# -*- coding: utf-8 -*-
'''
Created on 2014年11月19日

@author: osanllyer
'''
from sqlalchemy import *
from sqlalchemy.orm import *
from base import *
from firm import Firm

class Lawyer(Base):
    '''
    lawyer
    '''
    
    __tablename__ = 'lawyer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    headprotrait = Column(String)
    certificateId = Column(String)
    score = Column(Integer)
    firm = Column(Integer, ForeignKey('firm.id'))
    last_updated = Column(DateTime)
    
   
    
class LawyerLocation(Base):
    '''store lawyer locations realtime, so there maybe many writes , may be shourld use redis'''
    
    __tablename__ = 'lawyer_location'
    
    id = Column(Integer, primary_key=True)
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    longitude = Column(String)
    latitude = Column(String)
    last_updated = Column(DateTime)



if __name__ == '__main__':
    'test'
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(Firm(name="bobo", addr="taiwang"))
    # session.add(Lawyer(name="aaaa", firm=1, headprotrait="adfdsfsdf", certificateId=3))
    session.flush()
    session.commit()
    session.query(Firm)