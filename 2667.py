import queue

def valid(i, j) :
    global arr, visited, N
    
    if i < 0 or i >= N or j < 0 or j >= N or arr[i][j] == 0 :
        return False
    if visited[i][j] == True :
        return False
    return True

def BFS(i, j) :
    global arr, visited
    
    Q = queue.Queue()
    Q.put([i, j])
    visited[i][j] = True
    count = 1
    while Q.qsize() != 0 :
        i, j = Q.get()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
            if valid(i+dy, j+dx) :
                visited[i+dy][j+dx] = True
                count += 1
                Q.put([i+dy, j+dx])
    return count

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N) :
    M = input()
    for j in range(N) :
        arr[i][j] = int(M[j])

num = 0
result = []
for i in range(N) :
    for j in range(N) :
        if valid(i, j) :
            num += 1
            result.append(BFS(i, j))
result.sort()

print(num)
for i in result :
    print(i)