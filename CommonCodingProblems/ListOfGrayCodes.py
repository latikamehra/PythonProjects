class Solution:
    def isPowTwo(self, n) :
        xorRes = n&(n-1)
        if xorRes == 0 :
            return True
        else:
            return False
        
    def isGray(self, n1, n2):
        xorRes = n1^n2
        return self.isPowTwo(xorRes)
        
    def grayCode(self, n) :
        if n==0 : return [0]
        if n==1 : return [0,1]
        
        fin = (2**n)
        
        numSet = []
        for i in range(1,fin) :
            numSet.append(i)
            
        codes = []
        codes.append(0)
        
        for i in range(1,fin) :
            prev = codes[i-1] 
            for j in range(0, len(numSet)) :
                curr = numSet[j]
                if self.isGray(prev, curr) :
                    codes.append(curr)
                    numSet.remove(curr)
                    break
                    
        return codes