'''
from manageDuplicates import DisplayDuplicates as dd

print(dd.disp('/Users/latikamehra/Pictures/Jonny1/Jonny_ - 27.jpg', '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 27.jpg'))


print(dd.disp('/Users/latikamehra/Pictures/Jonny1/Jonny_ - 23.jpg', '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 24.jpg'))
'''

from imageanalysis import PixelData, BasicImageDetails, ExifData
from PIL import Image, ExifTags
import imageio
from manageDuplicates import DisplayDuplicates as dd

file1 = '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 9.jpg'
file2 = '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 10.jpg'


dd.disp(file1, file2)


pic = imageio.imread(file1)

exifData = ExifData.fetch(file1)

print(exifData['DateTimeOriginal'])

flst = [file1,file2]

print(BasicImageDetails.fetch(flst))

comp = PixelData.compare(file1, file2, threshold=150)

print (comp)