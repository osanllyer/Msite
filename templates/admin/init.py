# -*- coding: utf-8 -*-
'''
Created on 2014年11月19日

@author: osanllyer
'''
import os

from Model.base import *
from Model.firm import *
from Model.lawyer import *
 
from common.logger import *
logger = logging.getLogger(__file__)

class InitServer(object):
    '''inint all system settings'''
    def __init__(self):
        pass

    def init(self):
        pass

class InitDBs(object):
    '''init all tables and dbs'''
    def __init__(self):
        pass
    
    def init(self):
        'init all dbs'
        'if tables exists, do nothing'
        Base.metadata.create_all(bind=engine, checkfirst=True) 
        logger.info("finished init db tables")

def init():
    InitServer().init()
    InitDBs().init()
    
if __name__ == '__main__':
    init()    
