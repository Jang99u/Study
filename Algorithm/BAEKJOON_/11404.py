import sys

INF = 100000000
N = int(input())
M = int(input())
costarr = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M) :
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    start -= 1
    end -= 1
    costarr[start][end] = min(costarr[start][end], cost)
    
for i in range(N) :
    for j in range(N) :
        if j == i :
            continue
        for k in range(N) :
            if k == j :
                continue
            costarr[j][k] = min(costarr[j][k], costarr[j][i] + costarr[i][k])
            
for i in costarr :
    for j in i :
        if j == INF :
            print(0, end=" ")
        else :
            print(j, end=" ")
    print()