r, c = map(int, input().split())
i, j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
count = 0

def valid(i, j) :
    if i < 0 or j < 0 or i >= r or j >= c or visited[i][j] == True or arr[i][j] == 1 :
        return False
    return True
    
def can_clean(i, j) :
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
        if valid(i+dy, j+dx) :
            return True
    return False
        
def clean(i, j) :
    visited[i][j] = True

def go_forward(i, j, d) :
    if d == 0 :
        i -= 1
    if d == 1 :
        j += 1
    if d == 2 :
        i += 1
    if d == 3 :
        j -= 1
    return i, j

def go_back(i, j, d) :
    if d == 0 :
        i += 1
    if d == 1 :
        j -= 1
    if d == 2 :
        i -= 1
    if d == 3 :
        j += 1
    return i, j

def rotate(d) :
    if d == 0 :
        return 3
    else :
        return d-1
    
while True :
    if visited[i][j] == False :
        count += 1
        clean(i, j)
    
    if not can_clean(i, j) :
        i, j = go_back(i, j, d)
        
        if arr[i][j] == 1 :
            break
    else :
        d = rotate(d)
        i_, j_ = go_forward(i, j, d)
        
        if valid(i_, j_) :
            i, j = i_, j_
    
print(count)