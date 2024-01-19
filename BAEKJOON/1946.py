import sys
input = sys.stdin.readline

TC = int(input())
result = []
for _ in range(TC) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[0])
    
    cnt = 0
    minval = 0
    for i in range(N) :
        if i == 0 :
            cnt += 1
            minval = arr[i][1]
        else :
            if arr[i][1] < minval :
                cnt += 1
                minval = arr[i][1]
    result.append(str(cnt))
print("\n".join(result))