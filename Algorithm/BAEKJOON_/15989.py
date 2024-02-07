import sys
input = sys.stdin.readline

dp2 = [0, 1, 1, 1, 1, 2]
for i in range(6, 10001) :
    dp2.append(dp2[i-6] + 1)

dp = [1, 2, 3]    
for i in range(3, 10001) :
    dp.append(dp[i-1] + dp2[i])

N = int(input())
for _ in range(N) :
    print(dp[int(input())-1])