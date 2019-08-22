'''
from manageDuplicates import DisplayDuplicates as dd

print(dd.disp('/Users/latikamehra/Pictures/Jonny1/Jonny_ - 27.jpg', '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 27.jpg'))


print(dd.disp('/Users/latikamehra/Pictures/Jonny1/Jonny_ - 23.jpg', '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 24.jpg'))
'''


from imageanalysis import PixelData
from manageDuplicates import DisplayDuplicates as dd


file1 = '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 27.jpg'
file2 = '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 28.jpg'

cmp = PixelData.PixelData(threshold=50)

comp = cmp.compare(file1, file2)
print (comp)

dd.disp(file1, file2)

'''
pic1 = imageio.imread(file1)
pic2 = imageio.imread(file2)


for c in range(3) :
    print(pic1[ :, :, c].mean(), pic2[ :, :, c].mean())

exifData = ExifData.fetch(file2)

pp = ppr.PrettyPrint()
print(pp.collectionPrnt(exifData))

print(exifData['DateTimeOriginal'])

flst = [file1,file2]

print(BasicImageDetails.fetch(flst))

cmp = PixelData.PixelData(threshold='overview')

comp = cmp.compare(file1, file2)
print (comp)
'''