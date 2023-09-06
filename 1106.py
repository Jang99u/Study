C, N = map(int, input().split())

city = []
for _ in range(N) :
    city.append(list(map(int, input().split())))

dp = [0]
while dp[-1] < C :
    result = 0
    for i in range(N) :
        if city[i][0] <= len(dp) :
            result = max(result, dp[len(dp)-city[i][0]] + city[i][1])
    dp.append(result)

print(len(dp)-1)