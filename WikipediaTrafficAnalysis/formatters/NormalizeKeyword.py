'''
Created on Jul 29, 2019

@author: latikamehra
'''



def capitalizeFirstLetters(wrds):
    frmtdStr = []
    for w in wrds:
        capStr = w[0].upper() + w[1:]# Capitalize the first letter of the string WITHOUT changing case of the others
        frmtdStr.append(capStr)
    return (frmtdStr)


def title(strng):
    delims = [" ", "Mc", "Mac", "O'"]
    for delim in delims :
        wrds = strng.split(delim) 
        strng =  delim.join(capitalizeFirstLetters(wrds))  
    return strng
    