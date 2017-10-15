#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 8:33
# @Author  : Sugare
# @Site    : 30733705@qq.com
# @File    : urls.py
# @Software: PyCharm

from views import CustomersHandler, LoginHandler, AustomersHandler, FileHandler, ImageDataHandler, UserinfoHandler

handlers = [
    (r'/api/customer/(.*)', CustomersHandler),
    (r'/login', LoginHandler),
    (r'/aa', AustomersHandler),
    (r'/upload', FileHandler),
    (r'/imgdata', ImageDataHandler),
    (r'/user', UserinfoHandler)
]

