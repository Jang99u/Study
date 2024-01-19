A, B = map(int, input().split())
    
def func(num) :
    c = 2
    result = (num + 1) // 2 # 홀수 항들의 경우의 합
    while num >= 1 :
        num //= 2
        cnt = (num + 1) // 2
        result += cnt * c
        c *= 2
    return result

A -= 1
print(func(B) - func(A))