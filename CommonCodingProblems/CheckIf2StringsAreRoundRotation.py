'''
Created on Dec 4, 2019

@author: latikamehra
'''

def areRotations(string1, string2): 
    size1 = len(string1) 
    size2 = len(string2) 
  
    # Check if sizes of two strings are same 
    if size1 != size2: 
        return 0
  
    # Create a temp string with value str1.str1 
    temp = string1 + string1 
  
    # Now check if str2 is a substring of temp 
    # string.count returns the number of occurences of 
    # the second string in temp 
    if (string2 in temp): 
        return True
    else: 
        return False
  
# Driver program to test the above function 
string1 = "ABABAC"
string2 = "BACABA"
  
if areRotations(string1, string2): 
    print ("Strings are rotations of each other")
else: 
    print ("Strings are not rotations of each other")