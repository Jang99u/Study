import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def search(num) :
    global C, arr
    
    if visited[num] == True :
        return
    visited[num] = True
    
    for i in range(1, C+1) :
        if arr[num][i] == 1 :
            search(i)

C = int(input())
N = int(input())
arr = [[0 for _ in range(C+1)] for _ in range(C+1)]
visited = [False for _ in range(C+1)]

for _ in range(N) :
    c1, c2 = map(int, input().split())
    arr[c1][c2] = 1
    arr[c2][c1] = 1    

search(1)
result = 0
for i in visited :
    if i :
        result += 1
print(result-1)