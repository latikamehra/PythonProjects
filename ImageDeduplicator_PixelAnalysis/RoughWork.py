'''
from manageDuplicates import DisplayDuplicates as dd

print(dd.disp('/Users/latikamehra/Pictures/Jonny1/Jonny_ - 27.jpg', '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 27.jpg'))


print(dd.disp('/Users/latikamehra/Pictures/Jonny1/Jonny_ - 23.jpg', '/Users/latikamehra/Pictures/Jonny1/Jonny_ - 24.jpg'))
'''

from formatters import PrettyPrinter as pps

lstlst = [['/Users/latikamehra/Pictures/Jonny2/Jonny_ - 10.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 11.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 12.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 9.jpg'], 
['/Users/latikamehra/Pictures/Jonny2/AcousticFrameOfMind.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 7.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 1.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 2.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 8.jpg'], 
['/Users/latikamehra/Pictures/Jonny2/Jonny_ - 6.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 5.jpg'], 
['/Users/latikamehra/Pictures/Jonny2/Jonny_ - 4.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 3.jpg'], 
['/Users/latikamehra/Pictures/Jonny2/Jonny_ - 16.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 15.jpg'], 
['/Users/latikamehra/Pictures/Jonny2/Jonny_ - 24.jpg', '/Users/latikamehra/Pictures/Jonny2/Jonny_ - 23.jpg']]

def ops(mylstlst):
    
    for mylst in mylstlst :
        mylst.pop()



def opsStr(str1):
    str1 = "LookWhatHappened"+str1

ops(lstlst)

print (lstlst)


mystr = "Shit"
opsStr(mystr)

print(mystr)

