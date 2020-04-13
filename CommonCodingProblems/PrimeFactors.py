def isPrime(n):
    for i in range(2,n):
        if n%2 == 0 :
            return False 
    return True

def getPrimeFactors(num):
    if num == 1 : return [1]
    if isPrime(num) : return [num]
    
    for i in range(2,num):
        if isPrime(i) :
            if num%i == 0 :
                factors = [i]
                rem = num//i 
                factors += getPrimeFactors(rem)
                return factors
    
 
print (getPrimeFactors(24))   