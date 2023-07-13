import sys
sys.setrecursionlimit(10**6)

def Valid(r, c) :
    global Visited, Tomato, Row, Col
    if r < 0 or c < 0 or r >= Row or c >= Col or Visited[r][c] == True or Tomato[r][c] == -1 or Tomato[r][c] == 1 :
        return False
    return True

def Tomato_(r , c, lst_) :
    global Visited
    if Valid(r-1, c) :
        lst_.append([r-1, c])
        Visited[r-1][c] = True
    if Valid(r+1, c) :
        lst_.append([r+1, c])
        Visited[r+1][c] = True
    if Valid(r, c-1) :
        lst_.append([r, c-1])
        Visited[r][c-1] = True
    if Valid(r, c+1) :
        lst_.append([r, c+1])
        Visited[r][c+1] = True

def ChangeTomato(tomato) :
    global Tomato, Visited, Row, Col, count
        
    lst_ = []
    for i in range(len(tomato)) :
        Visited[tomato[i][0]][tomato[i][1]] = True
        Tomato[tomato[i][0]][tomato[i][1]] = 1
    
    for i in range(len(tomato)) :
        Tomato_(tomato[i][0], tomato[i][1], lst_)
    
    if len(lst_) == 0 :
        return
    count += 1
    ChangeTomato(lst_)
    
N = list(map(int, input("").split()))
Row = N[1]
Col = N[0]
Tomato = [[0 for _ in range(Col)] for _ in range(Row)]
Visited = [[False for _ in range(Col)] for _ in range(Row)]
count = 0

Start = []
for i in range(Row) :
    N = list(map(int, input("").split()))
    for j in range(Col) :
        Tomato[i][j] = N[j]
        if Tomato[i][j] == 1 :
            Start.append([i, j])
            
ChangeTomato(Start)

for i in range(Row) :
    for j in range(Col) :
        if Tomato[i][j] == 0 :
            print(-1)
            exit(0)
            
print(count)