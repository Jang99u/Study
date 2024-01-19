import queue

def valid(i, j, color) :
    global arr, visited, N
    
    if i < 0 or i >= N or j < 0 or j >= N or arr[i][j] == 0 :
        return False
    if visited[i][j] == True :
        return False
    if arr[i][j] != color :
        return False
    return True

def BFS(i, j, color) :
    global arr, visited
    
    Q = queue.Queue()
    Q.put([i, j])
    visited[i][j] = True
    while Q.qsize() != 0 :
        i, j = Q.get()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
            if valid(i+dy, j+dx, color) :
                visited[i+dy][j+dx] = True
                Q.put([i+dy, j+dx])

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N) :
    M = input()
    for j in range(N) :
        arr[i][j] = M[j]

num = 0
for i in range(N) :
    for j in range(N) :
        if valid(i, j, arr[i][j]) :
            num += 1
            BFS(i, j, arr[i][j])
print(num, end = " ")
          
num = 0  
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == "G" :
            arr[i][j] = "R"
            
for i in range(N) :
    for j in range(N) :
        if valid(i, j, arr[i][j]) :
            num += 1
            BFS(i, j, arr[i][j])
print(num)