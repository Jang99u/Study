import sys
input = sys.stdin.readline

N, TC = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N) :
    value = list(map(int, input().split()))
    for c in range(N) :
        if r > 0 and c > 0 :
            arr[r][c] = arr[r-1][c] + arr[r][c-1] - arr[r-1][c-1] + value[c]
        elif r <= 0 :
            arr[r][c] = arr[r][c-1] + value[c]
        elif c <= 0 :
            arr[r][c] = arr[r-1][c] + value[c]

result = []
for _ in range(TC) :
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = map(lambda x : x-1, [x1, y1, x2, y2])
    
    if x1 > 0 and y1 > 0 :
        cnt = arr[y2][x2] - (arr[y1-1][x2] + arr[y2][x1-1] - arr[y1-1][x1-1])
        result.append(str(cnt))
    elif x1 <= 0 and y1 <= 0 :
        cnt = arr[y2][x2]
        result.append(str(cnt))
    elif y1 <= 0 :
        cnt = arr[y2][x2] - arr[y2][x1-1]
        result.append(str(cnt))
    elif x1 <= 0 :
        cnt = arr[y2][x2] - arr[y1-1][x2]
        result.append(str(cnt))
print("\n".join(result))