import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N) :
    K = int(input())
    if K != 0 :
        stack.append(K)
    else :
        stack.pop()

print(sum(stack))