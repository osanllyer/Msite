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
    uid = Column(Integer, ForeignKey('customer.id'))
    content = Column(Text)
    ptype = Column(Integer, ForeignKey('posttype.id'))
    add_at = Column(DateTime)
    changed_at = Column(DateTime)
    
    