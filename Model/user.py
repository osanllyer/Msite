# -*- encoding:utf-8 -*-
'''
Created on Nov 26, 2014

@author: lifenbo
'''

from sqlalchemy import *
from sqlalchemy.orm import *
from base import *
from Model.base import *


class User(Base):
    '非律师普通用户'
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    headportrait = Column(String)
    score = Column(Integer)
    last_updated = Column(DateTime)
    '用户发的文章'
    posts = relationship('Posts')
