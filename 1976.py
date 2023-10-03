N = int(input())
M = int(input())
INF = 1000000

city = []
for _ in range(N) :
    city.append(list(map(int, input().split())))

for i in range(N) :
    for j in range(N) :
        if city[i][j] == 0 :
            city[i][j] = INF
            
for i in range(N) :
    for j in range(N) :
        if j == i :
            continue
        for k in range(N) :
            if k == j :
                continue
            city[j][k] = min(city[j][k], city[j][i] + city[i][k])
            
visit = list(map(int, input().split()))
for i in range(M-1) :
    start = visit[i] - 1
    end = visit[i+1] - 1
    if start == end :
        continue
    if city[start][end] >= INF :
        print("NO")
        exit()
print("YES")