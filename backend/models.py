#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/08/28 8:47
# @Author  : Sugare
# @File    : models.py
# @Software: PyCharm

from sqlalchemy import func, create_engine, Index, UniqueConstraint, and_, or_, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, DateTime, TEXT
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
import datetime

# connect to the database
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/crm?charset=utf8', pool_size=100)

# Base class
Base = declarative_base()

# Customer info
class CusInfo(Base):
    __tablename__ = 'cusinfo'
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(32))
    customer_addr = Column(String(32))
    customer_level = Column(Integer, default=0)     # 0为普通，1为vip
    customer_tel = Column(String(32))
    customer_people = Column(String(32))
    #customer_ctime = Column(DateTime, default=datetime.datetime.now())

    __table_args__ = (
        Index('ix_name_con', 'customer_name', 'customer_people'),
        Index('ix_name_tel', 'customer_name', 'customer_tel'),
    )

info1 = CusInfo(customer_id=1, customer_name="浦发银行", customer_addr="上海", customer_people="sugare", customer_tel="15641689860")
info2 = CusInfo(customer_id=2, customer_name="工商银行", customer_addr="北京", customer_people="张继", customer_tel="15641689860")
info3 = CusInfo(customer_id=3, customer_name="农业银行", customer_addr="北京", customer_people="Sugare", customer_tel="15641689860")
info4 = CusInfo(customer_id=4, customer_name="吉林银行", customer_addr="吉林", customer_people="等等", customer_tel="15641689860")



# Customer info
class UserInfo(Base):
    __tablename__ = 'userinfo'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(32))
    user_pass = Column(String(32))
    user_role = Column(Integer, default=0)     # 0为普通，1为vip
    user_img = Column(String(100))

    #customer_ctime = Column(DateTime, default=datetime.datetime.now())

    __table_args__ = (
        Index('ix_name_pass', 'user_name', 'user_pass'),
    )


user1 = UserInfo(user_name='sugare', user_pass='123456', user_role=0, user_img = 'http://127.0.0.1:8888/static/img/test-image.jpg')
user2 = UserInfo(user_name='test', user_pass='123456', user_role=1, user_img = 'http://127.0.0.1:8888/static/img/test-image.jpg')

MySession = sessionmaker(bind=engine)
conn = MySession()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # conn.query(CusInfo).filter(CusInfo.customer_id==1).update({CusInfo.customer_people: 'song', CusInfo.customer_level: 5})
    a = conn.query(UserInfo).filter(and_(UserInfo.user_name == 'test', UserInfo.user_pass == '123456')).first()
    a.user_pass = '123'
    print(a.user_pass)
    # print(a.user_img)
    # conn.add_all([user2,])
    # conntent = 'su'
    # tt = "%"+ conntent + "%"
    # c = conn.query(CusInfo).filter(CusInfo.customer_name.like(tt)).first()
    conn.commit()
    # print(a[0])
    # print(c.customer_name)

    pass