Q = [[0, 0]]
M = int(input(""))
NGELIST = list(map(int, input().split()))

NGEDICT = {}
for N in NGELIST :
    if N not in NGEDICT :
        NGEDICT[N] = 1
    else :
        NGEDICT[N] += 1
        
for i in range(M) :
    NGELIST[i] = [NGEDICT[NGELIST[i]], i+1, NGELIST[i]]
NGE = [-1 for _ in range(M+1)]

for N in NGELIST :
    POP = Q.pop()
    Q.append(POP)
    if N[0] > POP[0] :
        while len(Q) != 0 :
            POP = Q.pop()
            if POP[0] >= N[0] :
                Q.append(POP)
                break
            NGE[POP[1]] = N[2]
    Q.append(N)
    
for i in range(M) :
    print(NGE[i+1], end=" ")