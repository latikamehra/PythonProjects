'''
Created on Aug 16, 2019

@author: latikamehra
'''


from formatters import PrettyPrinter 
from pprint import pprint as pp

print ("12345\t1234567")

myDict = {"Radiohead" : {'Jonny': ['Guitar', "Synth", "Ondes Martenot"], 'Thom' : ['Guitar', 'Vocals']},
          "Beatles" : {'Paul': ('Bass', 'Vocals'), 'John' : ('Vocals', 'Guitar')},
          "Pink Floyd" : [['Waters', 'Bass'], ['Gilmore', 'Vocals']]
          }

pp(myDict)
pps = PrettyPrinter.PrettyPrint()
dt = pps.collectionPrnt(myDict)

print (dt)