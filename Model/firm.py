# -*- coding: utf-8 -*-
'''
Created on 2014年11月19日

@author: osanllyer
'''

from sqlalchemy import *
from sqlalchemy.orm import *
from base import *
from Model.lawyer import Lawyer

class Firm(Base):
    '''
    classdocs
    '''
    __tablename__ = 'firm'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    addr = Column(String)
    longitude = Column(String)
    latitude = Column(String)
    last_updated = Column(DateTime)
    'lawyers, 1n'
    lawyers = relationship('Lawyer', backref('firm'))
        