N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

def IsCan(num) :
    line = 0
    for i in arr :
        line += i // num
        if line >= K :
            return True    
    return False

start = 1
end = max(arr)
result = 0

if IsCan(end) :
    print(end)
    exit()

while start < end :
    mid = (start + end) // 2
    if IsCan(mid) :
        start = mid + 1
        result = max(result, mid)
    else :
        end = mid

print(result)