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