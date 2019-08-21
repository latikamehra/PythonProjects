'''
Created on Aug 21, 2019

@author: latikamehra
'''


from PIL import Image, ExifTags
from formatters import AppLogger as al


def fetch(f):
    log = al.logger.getChild(__name__)
    im = Image.open(f)
    exf = im._getexif()
    newexif = {}
    
    try :
        for k,v in exf.items() :
            tagKey = ExifTags.TAGS[k] # Change integer tag keys to actual values
            newexif[tagKey] = v
    except Exception as e:
        msg = "EXIF data for file "+f+" could not be fetched.\n"
        msg += str(type(e)) +" : "+ str(e)
        log.error(msg)
                
    
    return(newexif) 