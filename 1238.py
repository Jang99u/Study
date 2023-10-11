import heapq as hq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = 100000000
    
def dijkstra(X, city) :
    heap = [[0, X-1]]
    T = [INF for _ in range(N)]
    T[X-1] = 0
    while heap :
        cost, node = hq.heappop(heap)
        if T[node] < cost :
            continue
        
        for i in range(N) :
            if T[node] + city[node][i] < T[i] :
                T[i] = T[node] + city[node][i]
                hq.heappush(heap, [T[i], i])
                
    return T

city = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M) :
    start, end, cost = map(int, input().split())
    city[start-1][end-1] = cost
from_ = dijkstra(X, city)

for i in range(N) :
    for j in range(i, N) :
        city[i][j], city[j][i] = city[j][i], city[i][j]
to_ = dijkstra(X, city)

result = [from_[i] + to_[i] for i in range(N)]
print(max(result))

'''
# Floyd-Warshall
# Timeout

N, M, K = map(int, input().split())
INF = 1000000000
FW = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M) :
    start, end, time = map(int, input().split())
    FW[start-1][end-1] = time

for i in range(N) :
    for j in range(N) :
        if FW[j][i] == INF :
            continue
        if i == j :
            continue
        for k in range(N) :
            if j == k :
                continue
            FW[j][k] = min(FW[j][k], FW[j][i] + FW[i][k])

result = []
for i in range(N) :
    if i == K-1 :
        continue
    result.append(FW[i][K-1] + FW[K-1][i])
print(max(result))
'''