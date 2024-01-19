import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [[0 for _ in range(K+2)] for _ in range(N+2)]

for i in range(K+1) :
    bag[0][i+1] = i
for i in range(N) :
    bag[i+2][0] = list(map(int, input().split()))

for i in range(1, K+2) :
    for j in range(2, N+2) :
        W = bag[j][0][0]
        V = bag[j][0][1]
        
        if W > bag[0][i] :
            bag[j][i] = bag[j-1][i]
        elif W <= bag[0][i] :
            bag[j][i] = max(bag[j-1][i], bag[j-1][i-W] + V)

print(bag[N+1][K+1])