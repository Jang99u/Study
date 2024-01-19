N, K = map(int, input().split())
coin = []
for _ in range(N) :
    coin.append(int(input()))
coin.reverse()

result = 0
for i in coin :
    while i <= K :
        K -= i
        result += 1
    if K == 0:
        break
    
print(result)