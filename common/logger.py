'''
Created on Nov 24, 2014

@author: lifenbo
'''


import logging
import logging.config
import os


'''logger'''
logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "../configurations/logging.conf"))
