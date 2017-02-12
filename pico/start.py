#!/usr/bin/env python
# -*- coding: utf-8 -*-


from werkzeug.serving import run_simple
from pico.core import PicoServer, pico_path

server = PicoServer()
app = server.wsgi_app

run_simple('localhost', 8080, app, use_reloader=True,
           use_debugger=True,
           static_files={'/': './',
                         '/pico/client.js': pico_path + 'client.js'})
