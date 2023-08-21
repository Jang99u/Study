import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sum_ = 0
SUM = [0]
lst = list(map(int, input().split()))
for i in range(N) :
    sum_ += lst[i]
    SUM.append(sum_)
    
result = []
for _ in range(M) :
    i, j = map(int, input().split())
    result.append(str(SUM[j] - SUM[i-1]))

print("\n".join(result))