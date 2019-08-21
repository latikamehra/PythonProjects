'''
Created on Aug 16, 2019

@author: latikamehra
'''


lis1 = {1:11,2:22,4:44,5:55}
lis2 = {1:11,2:22,4:44,5:56}


if lis1 == lis2 :
    print ("Yaya")



from formatters import PrettyPrinter 
from pprint import pprint as pp

print ("12345\t1234567")

myDict = {"abcd": {"xyz" : {"qwert" : 1, "khwer": 3235456}, "ferghrhyt" : "weregrth"}, "rtrthyyrtrerytry" : 1243578}

'''
myDict = {"Radiohead" : {'Jonny': ['Guitar', "Synth", "Ondes Martenot"], 'Thom' : ['Guitar', 'Vocals']},
          "Beatles" : {'Paul': ('Bass', 'Vocals'), 'John' : ('Vocals', 'Guitar')},
          "Pink Floyd" : [['Waters', 'Bass'], ['Gilmore', 'Vocals']]
          }
'''

#pp(myDict)
pps = PrettyPrinter.PrettyPrint()
dt = pps.collectionPrnt(myDict)

print (dt)