import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def farming(r_, c_) :
    global visited, cabbage, r, c
    
    if r_ < 0 or c_ < 0 or r_ >= r or c_ >= c :
        return 0
    if visited[r_][c_] == True or cabbage[r_][c_] == 0 :
        return 0
    
    visited[r_][c_] = True
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
        farming(r_ + dy, c_ + dx)
    return 1

TC = int(input())
result = []
for _ in range(TC) :
    c, r, n = map(int, input().split())
    HowMany = 0
    visited = [[False for _ in range(c)] for _ in range(r)]
    cabbage = [[0 for _ in range(c)] for _ in range(r)]
    
    for _ in range(n) :
        C, R = map(int, input().split())
        cabbage[R][C] = 1

    for i in range(r) :
        for j in range(c) :
            HowMany += farming(i, j)

    result.append(str(HowMany))
    
print("\n".join(result))