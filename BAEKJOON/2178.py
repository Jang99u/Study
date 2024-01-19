import sys
import queue as Q
input = sys.stdin.readline

def BFS(r_, c_, count) :
    global maze, visited, r, c
    queue = Q.Queue()
    
    visited[r_][c_] = True
    queue.put([r_, c_, count])
    next = 1
    while queue.qsize() != 0 :
        for _ in range(next) :
            r_, c_, count_ = queue.get()
            if r_ == r-1 and c_ == c-1 :
                print(count_+1)
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
                if r_ + dr < 0 or c_ + dc < 0 or r_ + dr >= r or c_ + dc >= c :
                    continue
                elif visited[r_+dr][c_+dc] == True or maze[r_+dr][c_+dc] == '0' :
                    continue
                else : 
                    visited[r_+dr][c_+dc] = True
                    queue.put([r_+dr, c_+dc, count])
        next = queue.qsize()
        count += 1
                
r, c = map(int, input().split())
visited = [[False for _ in range(c)] for _ in range(r)]
maze = []
for i in range(r) :
    n = input()
    lst = []
    for j in range(c) :
        lst.append(n[j])
    maze.append(lst)
    
BFS(0, 0, 1)