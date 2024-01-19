import sys
sys.setrecursionlimit(10**6)

def DFS(r, c) :
    global Row, Column, Visited, Pixel
    if r < 0 or c < 0 or r > (Row - 1) or c > (Column - 1) or Pixel[r][c] == 0 or Visited[r][c] == True :
        return 
    Visited[r][c] = True
    for next in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
        DFS(r+next[0], c+next[1])
    
N = list(map(int, input("").split()))
Row = N[0]
Column = N[1]
Pixel = []
Visited = []

for i in range(Row) :
    lst = []
    lst_ = []
    N = list(map(int, input("").split()))
    for j in range(Column) :
        M = N[3*j:3*(j+1)]
        M = sum(M) / 3
        lst.append(M)
        lst_.append(False)
    Pixel.append(lst)
    Visited.append(lst_)

T = int(input(""))
for i in range(Row) :
    for j in range(Column) :
        if Pixel[i][j] >= T :
            Pixel[i][j] = 1
        else : 
            Pixel[i][j] = 0
          
HowManyItem = 0  
for i in range(Row) :
    for j in range(Column) :
        if Pixel[i][j] == 1 and Visited[i][j] == False :
            DFS(i, j)
            HowManyItem += 1

print(HowManyItem)