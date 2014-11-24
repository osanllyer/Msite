# -*- coding: utf-8 -*-
'''
Created on 2014年11月19日

@author: osanllyer
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine

Base = declarative_base()

engine = create_engine("sqlite://")

