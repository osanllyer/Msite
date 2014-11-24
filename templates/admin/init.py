'''
Created on 2014年11月19日

@author: osanllyer
'''
class InitServer(object):
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
        from Model.base import *
        from Model.firm import *
        from Model.lawyer import *
        
        Base.metadata.create_all(engine)


def init():
    InitServer().init();
    InitDBs().init();        