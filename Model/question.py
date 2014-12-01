# -*- encoding:utf-8 -*-
'''
Created on Nov 25, 2014

@author: lifenbo
'''
from sqlalchemy import *
from sqlalchemy.orm import *

from Model.base import *

class Posts(Base):
    '用户的提问'
    
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'))
    content = Column(Text)
    '问题分类'
    ptype = Column(Integer, ForeignKey('posttype.id'))

    add_at = Column(DateTime)
    changed_at = Column(DateTime)
    status = Column(SmallInteger)
    'answers, 1n'
    answers = relationship("Answer")
    
class Answer(Base):
    '律师对用户的回答'
    __tablename__ = 'answer'
    
    id = Column(Integer, primary_key=True)
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    content = Column(Text)
    add_at = Column(DateTime)
    changed_at = Column(DateTime)
    status = Column(SmallInteger)
    chosen = Column(Boolean)
    
    'relations'
    user = relationship("Lawyer")

class User(Base):
    '非律师普通用户'
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    headportrait = Column(String)
    score = Column(Integer)
    last_updated = Column(DateTime)
    '用户发的文章'
    posts = relationship('Posts', backref = backref("user"))

class PostType(Base):
    '问题类型'
    __tablename__ = 'posttype'
    id = Column(Integer, primary_key=True)
    type_name = Column(String)
    posts = relationship("Posts", backref = backref("PostType"))
    