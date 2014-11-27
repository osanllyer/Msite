# -*- coding: utf-8 -*-
'''
Created on 2014年11月19日

@author: osanllyer
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from configurations.conf import Configs
from sqlalchemy import *
from sqlalchemy.orm import *
import os

Base = declarative_base()

engine = create_engine("sqlite:///" + Configs.getAttr('db', 'dbfile'), echo=True, encoding='utf8', convert_unicode=True)
Session = sessionmaker(bind=engine)
session = Session()
