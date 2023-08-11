import sys
from itertools import combinations 
input = sys.stdin.readline

def nCr(n, r) :
    n = [i for i in range(n)]
    
    return len(list(combinations(n, r)))

TC = int(input())
result = []
for _ in range(TC) :
    r, n = map(int, input().split())
    result.append(nCr(n, r))
    
print(result)