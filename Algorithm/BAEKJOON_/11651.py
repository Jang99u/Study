import sys

N = int(input())
lst = []
for _ in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])
lst.sort(key = lambda x : (x[1], x[0]))

for i in lst :
    print(i[0], i[1])