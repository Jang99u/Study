import sys
input = sys.stdin.readline

N, M = map(int, input().split())

wordset = set([])
for _ in range(N) :
    wordset.add(input())
    
count = 0
for _ in range(M) :
    if input() in wordset :
        count += 1
        
print(count)