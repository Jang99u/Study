# 파이썬 메모리 초과 ㅠ
N = input()
M = input()
LCS = [[0 for _ in range(len(N)+1)] for _ in range(len(M)+1)]

for i in range(1, len(M)+1) :
    for j in range(1, len(N)+1) :
        if M[i-1] == N[j-1] :
            LCS[i][j] = LCS[i-1][j-1] + 1

print(max(list(map(lambda x : max(x), LCS))))