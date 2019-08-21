'''
Created on Aug 16, 2019

@author: latikamehra
'''

from PIL import Image, ExifTags
from pprint import pprint as pp


def fetch(f):

    im = Image.open(f)
    exf = im._getexif()
    newexif = {}
    
    for k,v in exf.items() :
        tagKey = ExifTags.TAGS[k] # Change integer tag keys to actual values
        newexif[tagKey] = v
    
    pp(newexif) 
    

if __name__ == "__main__":
    f = "/Users/latikamehra/Pictures/Jonny1/DuplicatesToReview/ToRemove/SecondaryCopy_5_0.jpg"
    fetch(f)
