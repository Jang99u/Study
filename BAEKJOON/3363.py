def find(lst, num) :
    for i in num :
        if i in lst :
            lst.remove(i)
    
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
bigger = num.copy()
lower = num.copy()

TC = []
for _ in range(3) :
    temp = input().rstrip().split()
    if not temp :
        temp = input().rstrip().split()
    TC.append(temp)

for lst in TC :
    left = list(map(int, lst[:4]))
    right = list(map(int, lst[5:]))
    lst_ = left.copy()
    lst_.extend(right)
    diff = list(set(num) - set(left) - set(right))
    
    if lst[4] == '<' :
        find(bigger, left)
        find(bigger, diff)
        find(lower, right)
        find(lower, diff)
    elif lst[4] == '>' :
        find(bigger, right)
        find(bigger, diff)
        find(lower, left)
        find(lower, diff)
    elif lst[4] == '=' :
        find(bigger, left)
        find(bigger, right)
        find(lower, left)
        find(lower, right)

if len(bigger) + len(lower) > 1 :
    print("indefinite")
elif len(bigger) + len(lower) == 0 :
    print("impossible")
else :
    if len(bigger) == 1 :
        print(str(bigger[0])+"+")
    elif len(lower) == 1 :
        print(str(lower[0])+"-")