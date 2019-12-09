'''
Created on Dec 3, 2019

@author: latikamehra'''

def xorFn(b1, b2):
    b1 = int(b1)
    b2= int(b2)
    if ((b1==0 and b2==0) or (b1==1 and b2==1)):
        return 0
    else:
        return 1
    
    

def binToGray(n):
    binStr = str(n)
    ln = len(binStr)
    
    gNum = binStr[0]
    
    for i in range(0, ln-1) :
        gNum = gNum + str(xorFn(binStr[i], binStr[i+1])) 
       
    return gNum


def grayToBin(n):
    grayStr = str(n)
    ln = len(grayStr)
    
    bNum = grayStr[0]
    lastBit = bNum
    
    for i in range(1, ln) :
        lastBit = str(xorFn(lastBit,grayStr[i]))
        bNum = bNum + lastBit
       
    return bNum


def binToDec(n):
    nstr = str(n)
    ln = len(nstr)
    dec = 0
    for i in range(0, ln) :
        cf= pow(2,ln-1-i)
        dec += int(nstr[i])*cf
        
    return (dec)

def checkNumPowOfTwo(n):
    andOp = n & (n-1)
    if n != 0 and andOp == 0 :
        return True
    else :
        return False


def checkGrayConsecutiveString(n1,n2):
    n1str = str(n1)
    n2str = str(n2)
    
    ln1 = len(n1str)
    ln2 = len(n2str)
    
    lndiff = ln1 - ln2
    
    if lndiff > 0 :
        n2str = "0"*lndiff + n2str
        ln = ln1
    elif lndiff < 0 :
        n1str = "0"*abs(lndiff) + n1str
        ln = ln2
        
         
    print (n1str)
    print (n2str)
    diff = 0 
    
    for i in range(0,ln) :
        if n1str[i] != n2str[i] :
            diff += 1
     
    #print (diff)       
    if diff != 1 :
        return False
    else :
        return True
        
    

def checkGrayConsequtiveBinary(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    xorVal = n1 ^ n2 # XOR of binary equivalent of the two integer numbers
    
    return (checkNumPowOfTwo(xorVal))

    
n1 = '011'
n2 = '100'
    
int1 = binToDec(n1)    
int2 = binToDec(n2)

print (checkGrayConsequtiveBinary(int1, int2))

#print (checkGrayConsequtiveBinary(3,'4'))       

#print (checkGrayConsecutiveString('1000111','111'))       
       
#print (binToGray(10110010))

#print (grayToBin(11101011))
    