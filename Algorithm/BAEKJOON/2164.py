from collections import deque

N = int(input())
Q = deque()

for i in range(N):
    i += 1
    Q.append(i)
    
while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())
    
print(Q[0])