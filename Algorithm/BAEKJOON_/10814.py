import sys

N = int(input())
arr = []
for i in range(N) :
    arr.append(sys.stdin.readline().split())
arr = sorted(arr, key = lambda x : int(x[0]))

result = []
for i in arr :
    result.append(" ".join(i))
print("\n".join(result))