dp = [1, 2]

for i in range(2, 1001) :
    cnt = dp[i-1] + dp[i-2]
    dp.append(cnt)

print(dp[int(input())-1] % 10007)