'''
Created on Aug 20, 2019

@author: latikamehra
'''

import os
import imageio
from formatters import AppLogger

def fetch(imgdir):
    log = AppLogger.logger.getChild(__name__)
    fls = os.listdir(imgdir)
    allFiles = [imgdir + f for f in fls]
    
    excpCntr = 0
    notImgFiles = []
    imgFiles = []
    
    for img in allFiles :
        try:
            pic = imageio.imread(img)
            imgFiles.append(img)

        except (AttributeError, OSError, IOError, ValueError) as a:
            excpCntr += 1
            notImgFiles.append(img)
            
            msg = str(excpCntr) +") "+ str(type(a)) +" : "+ str(a)
            msg += "\nThe following file does not appear to be an image file. Ignoring it for the list of consideration\n"
            msg += img
            
            log.error(msg)
            
            
    return imgFiles