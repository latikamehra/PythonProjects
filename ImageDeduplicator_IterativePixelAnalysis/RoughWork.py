'''
Created on Aug 26, 2019

@author: latikamehra
'''

from imageanalysis import PixelData

img1 = '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 7.jpg'
img2 = '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 1.jpg'

pd = PixelData.PixelData(threshold=0)

print(pd.chopAndCompare(img1,img2))

