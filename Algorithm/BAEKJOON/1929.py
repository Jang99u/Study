from math import sqrt

def IsDecimal(n) :
    if n == 1 :
        return False
    
    i = 2
    while i <= sqrt(n) :
        if n % i == 0 :
            return False
        i += 1
        
    return True

def FindDecimal(n, m) :
    for i in range(n, m+1) :
        if IsDecimal(i) :
            print(i)
            
n, m = map(int, input("").split())
FindDecimal(n, m)