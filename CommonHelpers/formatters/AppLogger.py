'''
Created on Jul 30, 2019

@author: latikamehra
'''

import logging
import os

#logDir = os.path.dirname(os.path.abspath(__file__))+"/../logs/"
#opDir = os.path.dirname(os.path.abspath(__file__))+"/../output/"


logger = logging.getLogger("main")

def createReqdDirs(mydir):
    if not os.path.exists(mydir):
        os.makedirs(mydir)

def initiate(logDir, fileName, lvl=logging.INFO, consoleFlag=True):
    createReqdDirs(logDir)
    fileName = logDir+fileName+".log"
    
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(fileName, mode='w')
    frmtr = logging.Formatter('[%(levelname)s] => %(name)s : \n\t%(message)s \n')
    
    file_handler.setFormatter(frmtr)
    console_handler.setFormatter(frmtr)
    
    logger.addHandler(file_handler)
    if consoleFlag == True : logger.addHandler(console_handler)
    logger.setLevel(lvl)
    

def prntr(name, opDir, fileName, consoleFlag=True):
    op = logging.getLogger(name)
    createReqdDirs(opDir)
    fileName = opDir+fileName+".txt"
    
    cns_hndlr = logging.StreamHandler()
    file_handler = logging.FileHandler(fileName, mode='w')
    frmtr = logging.Formatter('%(message)s')
    
    file_handler.setFormatter(frmtr)
    cns_hndlr.setFormatter(frmtr)
    
    op.addHandler(file_handler)
    if consoleFlag == True : op.addHandler(cns_hndlr)
    op.setLevel(logging.DEBUG)
    
    return(op)
    