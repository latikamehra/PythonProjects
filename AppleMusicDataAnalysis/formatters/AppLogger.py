'''
Created on Jul 30, 2019

@author: latikamehra
'''

import logging
import os

logger = logging.getLogger("main")
op = logging.getLogger("printer")

logDir = os.path.dirname(os.path.abspath(__file__))+"/../logs/"
opDir = os.path.dirname(os.path.abspath(__file__))+"/../output/"

def createReqdDirs(mydir):
    if not os.path.exists(mydir):
        os.makedirs(mydir)

def initiate(fileName, lvl=logging.INFO):
    createReqdDirs(logDir)
    fileName = logDir+fileName+".log"
    
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(fileName, mode='w')
    frmtr = logging.Formatter('[%(levelname)s] => %(name)s : \n\t%(message)s \n')
    
    file_handler.setFormatter(frmtr)
    console_handler.setFormatter(frmtr)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(lvl)
    

def prntr(fileName):
    createReqdDirs(opDir)
    fileName = opDir+fileName+".txt"
    
    cns_hndlr = logging.StreamHandler()
    file_handler = logging.FileHandler("output/"+fileName+".txt", mode='w')
    frmtr = logging.Formatter('%(message)s')
    
    file_handler.setFormatter(frmtr)
    cns_hndlr.setFormatter(frmtr)
    
    op.addHandler(file_handler)
    op.addHandler(cns_hndlr)
    op.setLevel(logging.DEBUG)
    