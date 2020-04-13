
def solution(A):
   maxN = max(A)
   flagArr = [0]*maxN
   
   for i in range(0,len(A)) :
       if A[i] > 0 :
           flagArr[A[i]-1] = 1
           
   for i in range(0,len(flagArr)) :
       if flagArr[i] == 0 :
           return i+1

   return maxN+1
        
            

            
print(solution([1, 3, 6, 4, 1, 2]))