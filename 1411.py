def StrToInt(string) :
    dic = {}
    cnt = 0
    result = []
    for i in string :
        if i not in dic :
           dic[i] = cnt
           result.append(str(cnt))
           cnt += 1
        else :
            result.append(str(dic[i]))
    return "".join(result)

def Factorial(n) :
    result = 1
    while n >= 1 :
        result *= n
        n -= 1
    return result

def Combination(n, r) :
    return Factorial(n) // (Factorial(r) * (Factorial(n-r)))

N = int(input())
lst = [StrToInt(input()) for _ in range(N)]

dic = {}
for i in lst :
    if i not in dic :
        dic[i] = 1
    else :
        dic[i] += 1

result = 0
for i in list(dic.keys()) :
    cnt = dic[i]
    result += Combination(cnt, 2)

print(result)