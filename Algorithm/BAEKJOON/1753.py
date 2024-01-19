import heapq as hq
import sys
input = sys.stdin.readline
print = sys.stdout.write

V, E = map(int, input().split())
K = int(input())
K -= 1
INF = 1000000000

def dijkstra(K) :
    global heap, road, T
    
    if K in road :
        for city in road[K] :
            if T[K] + road[K][city] < T[city] :
                T[city] = T[K] + road[K][city]
                hq.heappush(heap, [road[K][city], city])

heap = []
road = {}
for _ in range(E) :
    start, end, time = map(int, input().split())
    start -= 1
    end -= 1
    if start not in road :
        road[start] = {end : time}
    else :
        if end not in road[start] :
            road[start][end] = time
        else :
            road[start][end] = min(road[start][end], time)

T = [INF for _ in range(V)]
T[K] = 0

dijkstra(K)
while heap :
    D, K = hq.heappop(heap)
    
    if T[K] < D :
        continue
    else :
        dijkstra(K)

for i in T :
    if i == INF :
        print("INF" + '\n')
    else :
        print(str(i) + '\n')