N = int(input())
dpup = [1 for _ in range(N)]
dpdown = [1 for _ in range(N)]
arr = list(map(int, input().split()))

for i in range(N) :
    result = 1
    for j in range(i) :
        if arr[i] > arr[j] :
            result = max(result, dpup[j]+1)
    dpup[i] = result

arr.reverse()
for i in range(N) :
    result = 1
    for j in range(i) :
        if arr[i] > arr[j] :
            result = max(result, dpdown[j]+1)
    dpdown[i] = result
dpdown.reverse()

dp = [dpup[i] + dpdown[i] for i in range(N)]
print(max(dp)-1)