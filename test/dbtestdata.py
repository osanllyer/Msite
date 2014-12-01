# -*- encoding:utf-8 -*-
'''
Created on Nov 25, 2014

@author: lifenbo
'''


from sqlalchemy import *
from sqlalchemy.orm import *
from Model.base import *

from Model.firm import Firm
from Model.lawyer import Lawyer, LawyerLocation
from Model.question import *

def insertLawyerLocation():

    session.add(LawyerLocation(lawyer_id=1, longitude=116.435, latitude=39.993))
    session.add(LawyerLocation(lawyer_id=2, longitude=116.455, latitude=39.963))
    session.add(LawyerLocation(lawyer_id=3, longitude=116.355, latitude=40.063))
    
    session.commit()
    
    pass


def insertPostType():

    session.add(PostType(type_name='wedding'))
    
    pass

def insertPostsAndAnswers():

    session.add(Posts(uid=1, content='this is my question', ptype=1))
    session.add(Posts(uid=2, content='this is my question', ptype=1))
    session.add(Posts(uid=3, content='this is my question', ptype=1))
    session.add(Posts(uid=4, content='this is my question', ptype=1))
    session.add(Posts(uid=1, content='this is my question', ptype=1))
    session.add(Posts(uid=2, content='this is my question', ptype=1))
    session.add(Posts(uid=3, content='this is my question', ptype=1))
    session.add(Posts(uid=2, content='this is my question', ptype=1))
    session.add(Posts(uid=1, content='this is my question', ptype=1))

    session.add(Answer(lawyer_id=1, post_id=1, content="this is answer"))
    session.add(Answer(lawyer_id=2, post_id=2, content="this is answer"))
    session.add(Answer(lawyer_id=3, post_id=3, content="this is answer"))
    session.add(Answer(lawyer_id=3, post_id=4, content="this is answer"))
    session.add(Answer(lawyer_id=4, post_id=5, content="this is answer"))
    session.add(Answer(lawyer_id=5, post_id=6, content="this is answer"))
    session.add(Answer(lawyer_id=2, post_id=1, content="this is answer"))
    session.add(Answer(lawyer_id=1, post_id=1, content="this is answer"))
    
    session.commit



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

def insertLawyers():

    session.add(Lawyer(name=u"韩丽丽", firm_id=1, headportrait="a", certificate_id=3))
    session.add(Lawyer(name=u"李丽话", firm_id=2, headportrait="a", certificate_id=2))
    session.add(Lawyer(name=u"武钢", firm_id=3, headportrait="a", certificate_id=1))
    session.add(Lawyer(name=u"孙悟空", firm_id=1, headportrait="a", certificate_id=54))
    session.add(Lawyer(name=u"晨要紧", firm_id=5, headportrait="a", certificate_id=7))
    session.add(Lawyer(name=u"猪八戒", firm_id=4, headportrait="a", certificate_id=45))
    session.add(Lawyer(name=u"林黛玉", firm_id=3, headportrait="a", certificate_id=984))
    session.add(Lawyer(name=u"贾宝玉", firm_id=4, headportrait="a", certificate_id=231))
    session.add(Lawyer(name=u"毛泽东", firm_id=8, headportrait="a", certificate_id=11))
    session.add(Lawyer(name=u"林彪", firm_id=4, headportrait="a", certificate_id=87684))
    session.add(Lawyer(name=u"刘少奇", firm_id=6, headportrait="a", certificate_id=113))
    session.add(Lawyer(name=u"周恩来", firm_id=7, headportrait="a", certificate_id=432))
    session.add(Lawyer(name=u"薄熙来", firm_id=9, headportrait="a", certificate_id=873))
    session.add(Lawyer(name=u"习近平", firm_id=10, headportrait="a", certificate_id=1354))
    session.add(Lawyer(name=u"李鹏", firm_id=7, headportrait="a", certificate_id=55))
    session.add(Lawyer(name=u"江泽民", firm_id=3, headportrait="a", certificate_id=2321))
    
    session.commit()

def query():
    
   
    firms = session.query(Firm).filter_by(id=6).one()
    print firms.id, firms.name, firms.addr
    pass

def insert():
    insertFirms()
    insertLawyers()
    insertLawyerLocation()
    insertPostType()
    insertPostsAndAnswers()

if __name__ == '__main__':
    'test'
    insert()
#     query()
#     insertLawyerLocation()



    
    