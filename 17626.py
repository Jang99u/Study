from math import sqrt

dp = [0 for _ in range(50001)]
numlst = [i*i for i in range(1, 230)]
numset = set(numlst.copy())

N = int(input())
for i in range(1, N+1) :
    if i in numset :
        dp[i] = 1
    else :
        cnt = int(sqrt(i))
        key = 5
        lst = []
        for j in range(cnt) :
            key = min(key, dp[i-numlst[j]] + 1)
        dp[i] = key

print(dp[N])