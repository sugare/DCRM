#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 8:33
# @Author  : Sugare
# @Site    : 30733705@qq.com
# @File    : lib.py
# @Software: PyCharm


import jwt
import datetime
import base64
import json

def generateImage(strs, imgname, dir="./static/img/"):
    imgdata = base64.b64decode(strs)
    file = open(dir + '%s.jpg' % imgname, 'wb')
    file.write(imgdata)
    file.close()

def generateToken(username, exp=6000, SECRET=''):
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=exp)},
        SECRET,
        algorithm='HS256'
    )
    return token.decode('ascii')

def decryptToken(token, SECRET_KEY='', field=''):
    if field:
        return jwt.decode(token, SECRET_KEY)[field]
    else:
        return jwt.decode(token, SECRET_KEY)



def getJson(objs, prefix):
    if type(objs) != list:
        content = {}
        for field in dir(objs):
            if field.startswith(prefix):
                content[field] = objs.__getattribute__(field)
    else:
        content = []
        for obj in objs:
            data = {}
            for field in dir(obj):
                if field.startswith(prefix):
                    data[field] = obj.__getattribute__(field)
            content.append(data)
    return json.dumps(content)

AUTHORIZATION_HEADER = 'Authorization'
AUTHORIZATION_METHOD = 'bearer'
SECRET_KEY = "my_secret_key"
INVALID_HEADER_MESSAGE = "invalid header authorization"
MISSING_AUTHORIZATION_KEY = "Missing authorization"
AUTHORIZTION_ERROR_CODE = 401
SECRET = 'my_secret_key'

jwt_options = {
    'verify_signature': True,
    'verify_exp': True,
    'verify_nbf': False,
    'verify_iat': True,
    'verify_aud': False
}

def return_auth_error(handler, message):
    handler._transforms = []
    handler.set_status(AUTHORIZTION_ERROR_CODE)
    handler.write(message)

def return_header_error(handler):
    return_auth_error(handler, INVALID_HEADER_MESSAGE)

def is_valid_header(parts):
    """
    Authoriziton: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDM2NDE1ODYsInVzZXJuYW1lIjoic3VnYXJlIn0.PPhJZTv7JhNdcK65xxk30TqsB-9cnnzEPYntKUyWFHI

    :param parts:
    :return:
    """
    if parts[0].lower() != 'bearer':
        return False
    elif len(parts) == 1:
        return False
    elif len(parts) > 2:
        return False

    return True

if __name__ == '__main__':
    import random
    imgName = random.randint(1000000, 9999999)