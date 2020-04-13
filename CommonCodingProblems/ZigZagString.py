class Solution:
    def convert(self, s, numRows) :
        ln = len(s)
        
        row = 0
        dir = 1
        rws = [""] * numRows
        
        #if ln < numRows or numRows == 1 :
         #   return s
        
        for i in range(0,ln) :
            if row < numRows and row >= 0:
                rws[row] += s[i]
                print (row)
                print (rws[row]) 
                row += dir
            elif row >= numRows :
                dir = -1
                row -= 2
                rws[row] += s[i]
                print (row)
                print (rws[row])
            else :
                dir = 1
                row += 2
                rws[row] += s[i]
                print (row)
                print (rws[row])
            
               
        rslt = ""
        
        for rw in rws :
            print rw
            rslt += rw
            
        return rslt
    
    
sl = Solution()
print (sl.convert("PAYPALISHIRING", 3))

