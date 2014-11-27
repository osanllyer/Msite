# -*- coding: utf-8 -*-
'''
Created on 2014年11月19日

@author: osanllyer
'''
from sqlalchemy import *
from sqlalchemy.orm import *
from base import *
from Model.base import *

class Lawyer(Base):
    '''
    lawyer
    '''
    __tablename__ = 'lawyer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    headportrait = Column(String)
    certificate_id = Column(String)
    score = Column(Integer)
    firm_id = Column(Integer, ForeignKey('firm.id'))
    last_updated = Column(DateTime)
    
print Lawyer().__table__   
    
class LawyerLocation(Base):
    '''store lawyer locations realtime, so there maybe many writes , may be shourld use redis'''
    
    __tablename__ = 'lawyer_location'
    
    id = Column(Integer, primary_key=True)
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    longitude = Column(String)
    latitude = Column(String)
    last_updated = Column(DateTime)

class LawyerDao(object):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    sortmap = {
               "1":"id asc",
               }
    
    def getLawyerList(self, sort, start, num):
        '''获取指定数量的lawyer'''
        order = None
        if sort in LawyerDao.sortmap.keys():
            order = LawyerDao.sortmap[sort]
        else:
            'default order'
            order = LawyerDao.sortmap["1"]
            
        lawyers = LawyerDao.session.query(Lawyer).order_by(Lawyer.id)[start:start+num]
        
        return lawyers
        pass
        

