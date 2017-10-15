#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 8:33
# @Author  : Sugare
# @Site    : 30733705@qq.com
# @File    : view.py
# @Software: PyCharm

import tornado.web
from models import CusInfo, MySession, UserInfo
from lib import getJson, generateToken, decryptToken, is_valid_header,return_auth_error, return_header_error, generateImage
from sqlalchemy import and_, or_
import json
import os
import random

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.conn = MySession()

    def prepare(self):
        self.set_header("Access-Control-Allow-Headers", "Authorization")
        self.set_header("Access-Control-Allow-Origin", "*")

        auth = self.request.headers.get('Authorization')
        if auth:
            parts = auth.split()
            if not is_valid_header(parts):
                return_header_error(self)

            token = parts[1]
            try:
                decryptToken(token)
            except Exception as e:
                return_auth_error(self, str(e))
        else:
            self._transforms = []
            self.write("Missing authorization")
            self.finish()

    def options(self, *args, **kwargs):
        pass

class CustomersHandler(BaseHandler):
    def get(self, cid):
        if not cid:
            objs = self.conn.query(CusInfo).all()
            self.write(getJson(objs, "customer"))
        else:
            obj = self.conn.query(CusInfo).filter(CusInfo.customer_id == int(cid)).first()
            self.write(getJson(obj, "customer"))

    def post(self, *args, **kwargs):
        # print(self.request.body)
        # print(self.get_argument('customer_name'))
        #self.conn.add_all(self.request.body.decode('utf-8').split('&'))
        #self.conn.commit()
        customer_id = self.get_argument('customer_id')
        customer_name = self.get_argument('customer_name')
        customer_addr = self.get_argument('customer_addr')
        customer_people = self.get_argument('customer_people')
        customer_tel = self.get_argument('customer_tel')
        customer_level = self.get_argument('customer_level')
        if  customer_id:
            self.conn.query(CusInfo).filter(CusInfo.customer_id == customer_id).update({CusInfo.customer_name:customer_name,
                                                                                        CusInfo.customer_addr:customer_addr,
                                                                                        CusInfo.customer_people:customer_people,
                                                                                        CusInfo.customer_tel:customer_tel,
                                                                                        CusInfo.customer_level:customer_level})
        else:
            customer = CusInfo(customer_name=customer_name,
                               customer_addr=customer_addr,
                               customer_people=customer_people,
                               customer_tel=customer_tel,
                               customer_level=customer_level)
            self.conn.add_all([customer,])
        self.conn.commit()

class UserinfoHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        user_img = self.get_argument('user_img')
        user_name = self.get_argument('user_name')
        obj = self.conn.query(UserInfo).filter(UserInfo.user_name == user_name).first()
        obj.user_img = user_img
        self.conn.commit()
        self.write('ok')




class AustomersHandler(BaseHandler):
    def get(self):
        content = self.get_argument('title')

        objs = self.conn.query(CusInfo).filter(or_(CusInfo.customer_name.like("%" + content + "%"), CusInfo.customer_addr.like("%" + content + "%"), )).all()
        self.write(getJson(objs, "customer"))



class LoginHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.conn = MySession()

    def prepare(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        obj = self.conn.query(UserInfo).filter(and_(UserInfo.user_name == username, UserInfo.user_pass == password)).first()
        # if username == 'sugare' and password == '123456':
        if obj:
            response = {'token': generateToken(username, 6000)}
            userinfo = json.loads(getJson(obj, "user"))
            self.write(json.dumps(dict(response, **userinfo)))
        else:
            self.send_error(401)

    def options(self, *args, **kwargs):
        pass

class FileHandler(BaseHandler):
    def prepare(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def post(self, *args, **kwargs):
        file_metas = self.request.files['myFileName']

        for meta in file_metas:
            file_name = meta['filename']
            with open(os.path.join('static', 'img', file_name), 'wb') as up:
                up.write(meta['body'])

        self.set_header('ContentType', 'text/html')
        self.set_header('Charset', 'utf-8')
        imgUrl = '/static/img/%s' % file_name
        data = {'imgUrl': "http://127.0.0.1:8888" + imgUrl, "imgName":file_name}
        self.write(data)


class ImageDataHandler(BaseHandler):

    def post(self, *args, **kwargs):
        imgData = self.get_argument('imgData')
        imgName = random.randint(1000000, 9999999)
        generateImage(imgData.split(',')[1], imgname=str(imgName))
        data = {'imgDataUrl': "http://127.0.0.1:8888/static/img/" + str(imgName) + '.jpg'}
        print(data)
        self.write(data)
