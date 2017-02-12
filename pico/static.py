import time
import mimetypes
import re


class StaticServer(object):
    def __init__(self, arg):
        self.arg = arg

    def date_time_string(self, timestamp=None):
        """Return the current date and time formatted for a message header."""
        weekdayname = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        monthname = [None,
                     'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if timestamp is None:
            timestamp = time.time()
        year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
        s = "%s, %02d %3s %4d %02d:%02d:%02d GMT" % (weekdayname[wd],
                                                     day, monthname[month], year,
                                                     hh, mm, ss)
        return s

    def serve_file(self, file_path):
        response = Response()
        fs = os.stat(file_path)
        mimetype = mimetypes.guess_type(file_path)
        response.set_header("Content-length", str(fs.st_size))
        if file_path.endswith('.manifest'):
            response.set_header("Content-type", 'text/cache-manifest')
            response.set_header("Expires", 'access')
        else:
            response.set_header("Content-type", mimetype[0] or 'text/plain')
            response.set_header("Last-Modified", self.date_time_string(fs.st_mtime))
        response.content = open(file_path, 'rb')
        response.type = "file"
        return response

    def static_file_handler(self, path):
        file_path = ''
        for (url, directory) in STATIC_URL_MAP:
            m = re.match(url, path)
            if m:
                if '{0}' not in directory:
                    directory += '{0}'
                file_path = directory.format(*m.groups())

        # if the path does not point to a valid file, try default file
        file_exists = os.path.isfile(file_path)
        if not file_exists:
            file_path = os.path.join(file_path, DEFAULT)
        return self.serve_file(file_path)