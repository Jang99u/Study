N, K, L = map(int, input().split())
count = 1
while N > 1 :
    if abs(K - L) == 1 and min(K, L) % 2 == 1 :
        print(count)
        exit(0)
        
    count += 1
    if K % 2 == 0 :
        K = K // 2
    else :
        K = (K+1) // 2
    if L % 2 == 0 :
        L = L // 2
    else :
        L = (L+1) // 2
    N = (N // 2) + (N % 2)
print(-1)