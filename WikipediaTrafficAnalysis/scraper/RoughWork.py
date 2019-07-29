'''
Created on Jul 16, 2019

@author: latikamehra
'''

    
import logging



log = logging
log.basicConfig(filename='./XYZ.log', filemode='w',level=logging.INFO, format='\n %(message)s \n')

log.debug("Testing 123")