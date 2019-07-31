'''
Created on Jul 16, 2019

@author: latikamehra
'''

    
import logging


def rough():
    logger = logging.getLogger(__name__)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("logs/XYZ.log")
    frmtr = logging.Formatter('\n SUB : %(levelname)s %(message)s \n')
    
    file_handler.setFormatter(frmtr)
    console_handler.setFormatter(frmtr)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)
    
    #log.basicConfig(filename='./XYZ.log', filemode='w',level=logging.DEBUG, format='\n %(message)s \n')
    
    logger.info("Testing Sub")
    
