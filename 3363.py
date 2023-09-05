def canbigger(i) :
    global num, bigger, lower
    
    if i in bigger and i not in lower and len(bigger) == 1 :
        return True
    else :
        return False

def canlower(i) :
    global num, bigger, lower
    
    if i in lower and i not in bigger and len(lower) == 1 :
        return True
    else :
        return False
    
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
bigger = []
lower = []

TC = []
for _ in range(3) :
    temp = input().rstrip().split()
    if not temp :
        temp = input().rstrip().split()
    TC.append(temp)

for lst in TC :
    if lst[4] == '>' :
        bigger.append(set(map(int, lst[:4])))
        lower.append(set(map(int, lst[5:])))
    elif lst[4] == '<' :
        bigger.append(set(map(int, lst[5:])))
        lower.append(set(map(int, lst[:4])))
    elif lst[4] == '=' :
        bigger.append(set(num))
        lower.append(set(num))

bigger = bigger[0] & bigger[1] & bigger[2]
lower = lower[0] & lower[1] & lower[2]
if len(bigger) + len(lower) > 1 :
    print("indefinite")
    exit(0)

for i in num :
    if canbigger(i) :
        print(str(i)+"+")
        exit()
    if canlower(i) :
        print(str(i)+"-")
        exit()
print("impossible")