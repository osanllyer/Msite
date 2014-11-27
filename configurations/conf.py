# -*- coding:utf-8 -*-
'''
Created on Nov 24, 2014

@author: lifenbo
'''
import ConfigParser
import string, os, sys


class Configs(object):
    '''
    项目全局配置
    '''
    cf = ConfigParser.ConfigParser()
    cf.read(os.path.join(os.path.dirname(__file__), "site.conf"))
    
    @staticmethod
    def getAttr(sec, option):
        return Configs.cf.get(sec, option);
