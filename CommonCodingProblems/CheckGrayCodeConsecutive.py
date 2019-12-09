'''
Created on Dec 4, 2019

@author: latikamehra

Check if two binary encoded numbers are consecutive in Gray code
'''


def binToDec(n): # Converts Binary number to Decimal
    nstr = str(n)
    ln = len(nstr)
    dec = 0
    for i in range(0, ln) :
        cf= pow(2,ln-1-i)
        dec += int(nstr[i])*cf
        
    return (dec)

def checkNumPowOfTwo(n): # Check if a number if a power of 2. The AND operation on the binary equivalent of the number and (number - 1) should be 0 and the number itself should not be 0
    andOp = n & (n-1)
    if n != 0 and andOp == 0 :
        return True
    else :
        return False

def checkGrayConsequtiveBinary(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    xorVal = n1 ^ n2 # XOR of binary equivalent of the two integer numbers. This number should only contain one '1' in it for the numbers to be consecutive
    
    return (checkNumPowOfTwo(xorVal))

    
n1 = '100'
n2 = '110'
    
int1 = binToDec(n1)    
int2 = binToDec(n2)

print (checkGrayConsequtiveBinary(int1, int2))