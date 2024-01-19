L, R = list(map(int, input("").split()))
N = R-L
lL = len(str(L))
lR = len(str(R))

if lL != lR :
    print(0)
    exit(0)

digit = []
for i in range(lL) :
    strL = str(L)
    if strL[i] == '8' :
        digit.append(True)
    else :
        digit.append(False)

lst = []
lst.append('1')
for i in range(lR) :
    lst.append('0')
num = int("".join(lst))
numL = str(num - L)

lst = []
for i in range(len(str(num))) :
    try :
        lst.append(numL[-(i+1)])
    except :
        lst.append('0')
lst.reverse()

for i in range(lL) :
    check = digit[-(i+1)]
    if check == True :
        if i == 0 :
            if 0 < N :
                digit[-(i+1)] = False
                continue
            continue
        compare = int("".join(lst[(lL-(i-1)):]))    
        if compare == 0 :
            compare = 10**i
        if compare <= N :
            digit[-(i+1)] = False

num = 0
for i in digit :
    if i == True :
        num += 1
print(num)