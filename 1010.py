import sys
from itertools import combinations 
input = sys.stdin.readline

def factorial(n) :
    num = 1
    while n > 0 :
        num *= n
        n -= 1
        
    return num
        
def nCr(n, r) :
    return int((factorial(n) // factorial(n-r)) // factorial(r))

TC = int(input())
result = []
for _ in range(TC) :
    r, n = map(int, input().split())
    result.append(str(nCr(n, r)))
    
print("\n".join(result))