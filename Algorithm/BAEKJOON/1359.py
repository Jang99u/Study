from itertools import combinations

def nCr(n, r) :
    Arr = []
    for i in range(n) :
        Arr.append(i)
        
    return len(list(combinations(Arr, r)))

INPUT = list(map(int, input("").split()))
N = INPUT[0]
M = INPUT[1]
K = INPUT[2]

entire = nCr(N, M)
event = 0
lst = []
for i in range(M) :
    i += 1
    event_ = nCr(M, i) * nCr(N-M, M-i)
    if event_ == 0 :
        event_ = nCr(N, M)
    lst.append(event_)
    
for i in range(M) :
    i += 1
    if i >= K :
        event += lst[i-1]

prob = event/entire
if prob >= 1.0 :
    prob = 1.0
    
print(prob)