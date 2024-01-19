dp = [0, 0]
num = 2
while num <= 1000000 :
    dp_ = 1000000
    if num % 3 == 0 :
        dp_ = min(dp_, dp[num//3]+1)
    if num % 2 == 0 :
        dp_ = min(dp_, dp[num//2]+1)
    if num - 1 != 0 :    
        dp_ = min(dp_, dp[num-1]+1)
    dp.append(dp_)
    num += 1
    
print(dp[int(input())])