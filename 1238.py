N, M, C = map(int, input().split())
C -= 1
INF = 1000000000
dis = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N) :
    dis[i][i] = 0
    
for _ in range(M) :
    start, end, time = map(int, input().split())
    dis[start-1][end-1] = time
    
K = C
T = [INF for _ in range(N)]
visited = [False for _ in range(N)]
T[K] = 0
while False in visited :
    cnt = INF
    visited[K] = True
    for j in range(N) :
        time = T[K] + dis[K][j]
        T[j] = min(T[j], time)
        if dis[K][j] < cnt and visited[j] == False :
            cnt = dis[K][j]
            K_ = j
    K = K_
    
for i in range(N) :
    for j in range(i, N) :
        dis[i][j], dis[j][i] = dis[j][i], dis[i][j]
        
K = C
T_ = [INF for _ in range(N)]
visited = [False for _ in range(N)]
T_[K] = 0
while False in visited :
    cnt = INF
    visited[K] = True
    for j in range(N) :
        time = T_[K] + dis[K][j]
        T_[j] = min(T_[j], time)
        if dis[K][j] < cnt and visited[j] == False :
            cnt = dis[K][j]
            K_ = j
    K = K_

result = [T[i] + T_[i] for i in range(N)]
print(max(result))