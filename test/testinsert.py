# -*- encoding:utf-8 -*-
'''
Created on Nov 26, 2014

@author: lifenbo
'''
from sqlalchemy import *
from sqlalchemy.orm import *
from Model.base import *

from Model.firm import Firm
from Model.user import User

def insertUsers():

    
    session.add(User(name="aaaaaaaaa", headportrait="aaaa", score="23"))
    session.add(User(name="bbbb", headportrait="aaaa", score="2"))
    session.add(User(name="cccc", headportrait="aaaa", score="0"))
    session.add(User(name="dddd", headportrait="aaaa", score="34"))
    session.add(User(name="eeee", headportrait="aaaa", score="653"))
    session.add(User(name="fffff", headportrait="aaaa", score="3"))
    session.add(User(name="ggggg", headportrait="aaaa", score="1"))
    
    session.commit();
    pass

def insertFirms():

    session.add(Firm(name=u"安博律师事务所", addr=u"北京市大望路8号", longitude="116.435", latitude="39.993"))
    session.add(Firm(name=u"京豪律师事务所", addr=u"北京市西城区8号", longitude="116.464", latitude="39.948"))
    session.add(Firm(name=u"中银律师事务所", addr=u"北京市大兴区兴政街8号", longitude="116.376", latitude="40.012"))
    session.add(Firm(name=u"盈科律师事务所", addr=u"北京市朝阳路8号", longitude="116.343", latitude="39.957"))
    session.add(Firm(name=u"大同律师事务所", addr=u"北京市海淀路8号", longitude="116.224", latitude="39.871"))
    session.add(Firm(name=u"博昌律师事务所", addr=u"北京市石景山路8号", longitude="116.394", latitude="39.847"))
    session.add(Firm(name=u"月谈律师事务所", addr=u"北京市怀柔路8号", longitude="116.495", latitude="39.808"))
    session.add(Firm(name=u"美芮律师事务所", addr=u"北京市密云路8号", longitude="116.317", latitude="39.784"))
    session.add(Firm(name=u"豪杰律师事务所", addr=u"北京市顺义路8号", longitude="116.234", latitude="39.924"))
    session.add(Firm(name=u"中外律师事务所", addr=u"北京市昌平路8号", longitude="116.105", latitude="40.015"))
    
    session.commit()
    
insertFirms()
insertUsers()