N = int(input())
stair = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N+1)]
for i in range(N) :
    if i == 0 :
        dp[1] = stair[0]
    elif i == 1 :
        dp[2] = stair[0] + stair[1]
    else :
        dp[i+1] = max(dp[i-2] + stair[i-1] + stair[i], dp[i-1] + stair[i])

print(dp[-1])