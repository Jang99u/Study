import sys
input = sys.stdin.readline

def Euclid(a, b) :
    if b == 0 :
        return a
    else :
        return Euclid(b, a % b)
    
TC = int(input())
result = []
for _ in range(TC) :
    arr = list(map(int, input().split()))
    maxval = 0
    for i in range(len(arr)) :
        for j in range(len(arr)) :
            if i == j : continue
            a = max(arr[i], arr[j])
            b = min(arr[i], arr[j])
            maxval = max(maxval, Euclid(a, b))
    result.append(str(maxval))
print("\n".join(result))