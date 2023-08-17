def IsHansoo(num) :
    if num < 10 :
        return True
    
    num = str(num)
    d = int(num[1]) - int(num[0])
    for i in range(len(num)-1) :
        d_ = int(num[i+1]) - int(num[i])
        if d_ == d :
            d = d_
        else : 
            return False
    return True

N = int(input())
result = 0
for i in range(1, N+1) :
    if IsHansoo(i) :
        result += 1
print(result)