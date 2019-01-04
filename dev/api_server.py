#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid
import time
import json
import urllib.request
import threading
import socket
import socketserver
import http.server

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
API_DIR = os.path.join(ROOT_DIR, 'data', 'server')


# class Handler(http.server.SimpleHTTPRequestHandler, object):
#     def translate_path(self, path):
#         path = super(Handler, self).translate_path(path)
#         relpath = os.path.relpath(path, os.curdir)
#         return os.path.join(API_DIR, relpath)

PROXIED_URLS = dict()
SEMAPHORE = threading.Semaphore()

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path in PROXIED_URLS:
            path = PROXIED_URLS[self.path]
        else:
            path = "https://api.librepcb.org" + self.path
        content = urllib.request.urlopen(path).read()
        if self.path == '/api/v1/libraries/v0.1':
            j = json.loads(content.decode("utf-8"))
            for lib in j['results']:
                old_url = lib['icon_url']
                new_url = '/' + str(uuid.uuid4())
                PROXIED_URLS[new_url] = old_url
                lib['icon_url'] = 'http://localhost:50080' + new_url
            content = json.dumps(j).encode("utf-8")
        self.wfile.write(content)
        self.wfile.flush()
        SEMAPHORE.acquire()


class ApiServer:
    """
    Provides a HTTP server at localhost:50080
    """
    def __init__(self):
        # Set SO_REUSEADDR option to avoid "port already in use" errors
        self.httpd = socketserver.TCPServer(("", 50080), Proxy, bind_and_activate=False)
        self.httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.httpd.server_bind()
        self.httpd.server_activate()
        self.thread = threading.Thread(target=self.httpd.serve_forever)
        self.thread.daemon = True
        self.thread.start()
        time.sleep(0.2)  # wait a bit to make sure the server is ready

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def process(self):
        SEMAPHORE.release()



