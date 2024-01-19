import copy
from itertools import combinations

def valid(i, j) :
    global new_lab, visited
        
    if i < 0 or j < 0 or i >= r or j >= c or visited[i][j] == True or new_lab[i][j] != 0 :
        return False
    return True

def dfs(i, j) :
    global new_lab, visited
    
    visited[i][j] = True
    new_lab[i][j] = 2
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
        if valid(i+dy, j+dx) :
            dfs(i+dy, j+dx)

def search(lab) :
    lst = []
    for i in range(r) :
        for j in range(c) :
            if lab[i][j] == 2 :
                lst.append([i, j])
    return lst

r, c = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(r)]
result = 0
room = []
for i in range(r) :
    for j in range(c) :
        if lab[i][j] == 0 :
            room.append([i, j])
    
lst = list(combinations(room, 3))
for lst_ in lst :
    ir, ic = lst_[0]
    jr, jc = lst_[1]
    kr, kc = lst_[2]
    new_lab = copy.deepcopy(lab)
    visited = [[False for _ in range(c)] for _ in range(r)]
    new_lab[ir][ic], new_lab[jr][jc], new_lab[kr][kc] = 1, 1, 1
    
    virus = search(new_lab) 
    for i, j in virus :
        dfs(i, j)
    
    cnt = 0
    for i in range(r) :
        for j in range(c) :
            if new_lab[i][j] == 0 :
                cnt += 1
    result = max(result, cnt)
            
print(result)