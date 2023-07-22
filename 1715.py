import sys 
import heapq

M = int(input(""))
HQ = []
N = [int(sys.stdin.readline().strip()) for i in range(M)]

for i in N :
    heapq.heappush(HQ, i)

if M == 1 :
    print(0)
    exit(0)

result = 0
while 1 :
    POP1 = heapq.heappop(HQ)
    POP2 = heapq.heappop(HQ)
    NEW = POP1 + POP2
    result += NEW
    
    if len(HQ) == 0 :
        break
    
    heapq.heappush(HQ, NEW)

print(result)

# Timeout
'''
import sys
from collections import deque

M = int(input(""))
N = [int(sys.stdin.readline().strip()) for i in range(M)]
N.sort()
Q = deque(N)

if M == 1 :
    print(N[0])
    exit(0)

result = 0
while 1 :
    POP_1 = Q.popleft()
    POP_2 = Q.popleft()
    NEW = POP_1 + POP_2
    result += NEW
    
    if len(Q) == 0 :
        break
        
    lst = []
    while len(Q) != 0 :
        POP = Q.popleft()
        if POP >= NEW :
            Q.appendleft(POP)
            break
        lst.append(POP)
    
    Q.appendleft(NEW)
    for _ in range(len(lst)) :
        Q.appendleft(lst.pop())

print(result)
'''