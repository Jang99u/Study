import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N) :
    T, S = map(int, input().split())
    time.append([T, S])
time.sort(key= lambda x : x[1])

gap = 1000000
stack = []
for i in time :
    stack.append(i[0])
    if sum(stack) > i[1] :
        print(-1)
        exit(0)
    gap = min(gap, i[1]-sum(stack))
    
print(gap)