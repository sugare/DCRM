#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 8:33
# @Author  : Sugare
# @Site    : 30733705@qq.com
# @File    : app.py
# @Software: PyCharm

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options
from urls import handlers
import os

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            # xsrf_cookies=True,
            # login_url="/",
            # debug=True,
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
        )
        super(Application, self).__init__(handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()