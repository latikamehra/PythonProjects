def isPalin(s) :
        if len(s) <= 1 :
            return True
        elif s[0] == s[-1] :
            return isPalin(s[1:-1])
        else : return False

def longestPalin(s):
    if len(s) <= 1 : return s
    for palinLength in range(len(s), 0, -1) :
        print (palinLength)
        for i in range(0, (len(s) - palinLength) + 1) :
            substr = s[i : (i+palinLength)]
            print (substr)
            if isPalin(substr) : return substr        
        
print (longestPalin("aa"))