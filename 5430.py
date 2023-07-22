from collections import deque

def AC(F, DQ) :
    IsReverse = False
    for i in F :
        if i == 'R' :
            IsReverse = not IsReverse
        if i == 'D' :
            if len(DQ) == 0 :
                return "error"
            if IsReverse == False :
                DQ.popleft()
            else :
                DQ.pop()
    return [DQ, IsReverse]           

TC = int(input())
result = []
for _ in range(TC) :
    
    Function = input()
    size = int(input())
    Arr = input()
    if size == 0 :
        DQ = deque([])
        result.append(AC(Function, DQ))
        continue
    Arr = list(map(int, Arr[1:len(Arr)-1].split(",")))
    DQ = deque(Arr)
        
    result.append(AC(Function, DQ))
    
for i in result :
    if i == 'error' :
        print('error')
        continue
    if i[1] == False :
        print("[",end="")
        while len(i[0]) != 0 :
            if len(i[0]) == 1 :
                print(i[0].popleft(),end="")
                continue    
            print(i[0].popleft(),end=",")
        print("]")
    elif i[1] == True :
        print("[",end="")
        while len(i[0]) != 0 :
            if len(i[0]) == 1 :
                print(i[0].pop(),end="")
                continue    
            print(i[0].pop(),end=",")
        print("]")