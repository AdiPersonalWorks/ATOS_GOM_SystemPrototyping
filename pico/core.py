import sys
import cgi
import json
import os

import traceback

import pico
import pico.modules

from pico import PicoError, Response

pico_path = (os.path.dirname(__file__) or '.') + '/'
_server_process = None
pico_exports = []


class APIError(Exception):
    pass


class PicoServer(object):
    def __init__(self):
        pass

    def call_function(self, module, function_name, parameters):
        try:
            f = getattr(module, function_name)
        except AttributeError:
            raise Exception("No matching function availble. "
                            "You asked for %s with these parameters %s!" % (
                                function_name, parameters))
        results = f(**parameters)
        response = Response(content=results)
        if hasattr(f, 'cacheable') and f.cacheable:
            response.cacheable = True
        if hasattr(f, 'stream') and f.stream and STREAMING:
            response.type = "stream"
        elif response.content.__class__.__name__ == 'generator':
            response.type = "chunks"
        return response

    def call_method(self, module, class_name, method_name, parameters,
                    init_args):
        try:
            cls = getattr(module, class_name)
            obj = cls(*init_args)
        except KeyError:
            raise Exception("No matching class availble."
                            "You asked for %s!" % (class_name))
        r = self.call_function(obj, method_name, parameters)
        return r

    def _call(self, module_name, function_name, args, class_name=None,
              init_args=None):
        module = pico.modules.load(module_name)
        json_loaders = getattr(module, "json_loaders", [])
        from_json = lambda s: pico.from_json(s, json_loaders)
        for k in args:
            args[k] = from_json(args[k])
        if class_name:
            init_args = map(from_json, init_args)
            response = self.call_method(module, class_name, function_name,
                                        args, init_args)
        else:
            response = self.call_function(module, function_name, args)
        response.json_dumpers = getattr(module, "json_dumpers", {})
        return response

    def call(self, module_name, class_name, function_name, params):
        callback = params.get('_callback', None)
        init_args = json.loads(params.get('_init', '[]'))
        args = self._parse_args(params)
        response = self._call(module_name, function_name, args, class_name,
                              init_args)
        response.callback = callback
        return response

    def _parse_args(self, params):
        args = {}
        for k in params.keys():
            if not (k.startswith('_') or k.startswith('pico_')):
                params[k] = params[k].decode('utf-8')
                try:
                    args[k] = json.loads(params[k])
                except Exception:
                    try:
                        args[k] = json.loads(params[k].replace("'", '"'))
                    except Exception:
                        args[k] = params[k]
        return args

    def _load(self, module_name, params):
        params['_module'] = 'pico.modules'
        params['_function'] = 'load'
        params['module_name'] = '"%s"' % module_name
        return self.call('pico.modules', None, 'load', params)

    def log(self, *args):
        if not SILENT:
            print(args[0] if len(args) == 1 else args)

    def extract_params(self, environ):
        params = {}
        content_type = environ.get('CONTENT_TYPE', '')
        content_type, opts = cgi.parse_header(content_type)
        # now get GET and POST data
        print(content_type)
        if content_type == 'application/json':
            length = int(environ.get('CONTENT_LENGTH', '0'))
            json_params = json.loads(environ['wsgi.input'].read(length))
            params.update(json_params)
        else:
            pass
            # fields = cgi.FieldStorage(fp=environ['wsgi.input'],
            #                           environ=environ)
            # for name in fields:
            #     if fields[name].filename:
            #         upload = fields[name]
            #         params[name] = upload.file
            #     elif type(fields[name]) == list and fields[name][0].file:
            #         params[name] = [v.file for v in fields[name]]
            #     else:
            #         params[name] = fields[name].value
        return params

    def generate_exception_report(self, e, path, params):
        response = Response()
        report = {}
        report['exception'] = str(e)
        if DEBUG:
            full_tb = traceback.extract_tb(sys.exc_info()[2])
            tb_str = ''
            for tb in full_tb:
                tb_str += "File '%s', line %s, in %s; " % (tb[0], tb[1], tb[2])
            report['traceback'] = tb_str
        report['url'] = path.replace('/pico/', '/')
        report['params'] = dict([(k, _value_summary(params[k]))
                                for k in params])
        self.log(json.dumps(report, indent=1))
        response.content = report
        response.status = '500 ' + str(e)
        return response

    def handle_api_v2(self, path, params, request):
        # nice urls:
        #   /module_name/
        #   /module_name/function_name/?foo=bar
        #   /module_name/function_name/foo=bar # not implemented!
        #   /module_name/function_name/bar # not implemented!
        #   /module_name/class_name/function_name/
        parts = [p for p in path.split('/') if p]
        print(parts)
        if len(parts) == 1:
            return self._load(parts[0], params)
        else:
            if len(parts) == 2:
                module_name = parts[0]
                class_name = None
                function_name = parts[1]
            else:
                module_name = parts[0]
                class_name = parts[1]
                function_name = parts[2]
            return self.call(module_name, class_name, function_name, params)
        raise APIError(path)

    def wsgi_app(self, environ, start_response, enable_static=False):
        if environ['REQUEST_METHOD'] == 'OPTIONS':
            # This is to hanle the preflight request for CORS.
            # See https://developer.mozilla.org/en/http_access_control
            response = Response()
            response.status = "200 OK"
        else:
            params = self.extract_params(environ)
            self.log('------')
            path = environ['PATH_INFO'].split(environ['HTTP_HOST'])[-1]
            if BASE_PATH:
                path = path.split(BASE_PATH)[1]
            self.log(path)
            path = path.replace('/pico/', '/')
            try:
                response = self.handle_api_v2(path, params, environ)
            except PicoError, e:
                response = e.response
            except False, e:
                response = self.generate_exception_report(e, path, params)
        start_response(response.status, response.headers)
        return response.output

    def wsgi_dev_app(self, environ, start_response):
        return self.wsgi_app(environ, start_response, enable_static=True)


def _value_summary(value):
    s = repr(value)
    if len(s) > 100:
        s = s[:100] + '...'
    return s


CACHE_PATH = './cache/'
BASE_PATH = ''
STATIC_URL_MAP = [
    ('^/(.*)$', './'),
]
DEFAULT = 'index.html'
RELOAD = True
STREAMING = False
SILENT = False
DEBUG = False
