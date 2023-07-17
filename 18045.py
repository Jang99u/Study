def Valid(r, c) :
    global SIZE, space
    if r < 0 or c < 0 or r >= SIZE or c >= SIZE or space[r][c] != 0 :
        return False
    else :
        return True

def Injection(virusnum, lst) :
    global space
    
    result = []
    for virus in lst :
        r = virus[0]
        c = virus[1]
        for dx, dy in [-1,0],[1,0],[0,-1],[0,1] :
            if Valid(r+dy, c+dx) :
                space[r+dy][c+dx] = virusnum
                result.append([r+dy, c+dx])
    return result

SIZE, K = map(int, input("").split())

space = []
virus = {}
for i in range(SIZE) :
    lst = []
    N = list(map(int,input("").split()))
    for j in range(SIZE) :
        lst.append(N[j])
        if N[j] != 0 :
            if N[j] in virus :
                virus[N[j]].append([i, j])
            else :
                virus[N[j]] = [[i, j]]
    space.append(lst)
virus = dict(sorted(virus.items()))

Time, r, c = map(int, input("").split())
for _ in range(Time) :
    for i, j in zip(virus, virus.values()) :
        virus[i] = Injection(i, j)

print(space[r-1][c-1])