'''
Created on Jul 30, 2019

@author: latikamehra
'''

import logging

logger = logging.getLogger("main")
op = logging.getLogger("printer")

def initiate(fileName, lvl=logging.INFO):
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("logs/"+fileName+".log", mode='w')
    frmtr = logging.Formatter('[%(levelname)s] => %(name)s : \n\t%(message)s \n')
    
    file_handler.setFormatter(frmtr)
    console_handler.setFormatter(frmtr)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(lvl)
    

def prntr(fileName):
    cns_hndlr = logging.StreamHandler()
    file_handler = logging.FileHandler("output/"+fileName+".txt", mode='w')
    frmtr = logging.Formatter('%(message)s')
    
    file_handler.setFormatter(frmtr)
    cns_hndlr.setFormatter(frmtr)
    
    op.addHandler(file_handler)
    op.addHandler(cns_hndlr)
    op.setLevel(logging.DEBUG)
    