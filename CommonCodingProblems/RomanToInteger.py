class Solution:
    def toBeDeducted(self, c1, c2) :
        if c1 == 'I' and c2 in ('V', 'X') :
            return True
        if c1 == 'X' and c2 in ('L', 'C') :
            return True
        if c1 == 'C' and c2 in ('D', 'M') :
            return True
        return False
        
    def romanToInt(self, s):       
        lkpMap = {'I' : 1,
                  'V' : 5,
                  'X' : 10,
                  'L' : 50,
                  'C' : 100,
                  'D' : 500,
                  'M' : 1000
        }
        intVal = 0
        skipNext = False
        for i in range(0,len(s)-1) :
            if skipNext == False :
                print (intVal)
                char1 = s[i]
                char2 = s[i+1]
                
                print (char1)
                
                dedCheck = self.toBeDeducted(char1, char2)
                if dedCheck == True :
                    intVal += lkpMap[char2] - lkpMap[char1]
                    skipNext = True
                else :
                    intVal += lkpMap[char1]
                    skipNext = False
                    
            else :
                skipNext = False
    
        if skipNext == False :
            intVal += lkpMap[s[-1]]
            
        return intVal

    
            
ip = "MCMXCIV"            
obj = Solution()
print obj.romanToInt(ip)      