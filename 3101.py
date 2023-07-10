N = list(map(int, input("").split()))
Size = N[0]
jump = N[1]
ArrSize = Size*2-1

StartNum = []
for i in range(ArrSize) :
    StartNum.append(0)
    
for i in range(Size) :
    if i == 0 :
        StartNum[0] = 1
        StartNum[-(i+1)] = Size**2
    elif i % 2 != 0 :
        StartNum[i] = StartNum[i-1] + 1
        if i+1 != Size :
            StartNum[-(i+1)] = StartNum[-i] - 1
    else : 
        StartNum[i] = StartNum[i-1] + 4*(i//2)
        if i+1 != Size :
            StartNum[-(i+1)] = StartNum[-i] - 4*(i//2)

N = input("")
result = 1
IndexR = 0
IndexC = 0
for i in range(jump) :
    if N[i] == "U" :
        IndexR -= 1
    if N[i] == "D" :
        IndexR += 1
    if N[i] == "L" :
        IndexC -= 1
    if N[i] == "R" :
        IndexC += 1
    Index = IndexR + IndexC

    if Index < Size :
        lst = []
        lst.append(StartNum[Index])
        if Index % 2 != 0 :
            result += lst[0] + IndexR
        else : 
            result += lst[0] - IndexR
        
    
    elif Index >= Size :
        lst = []
        lst.append(StartNum[Index])
        if Index % 2 != 0 :
            IndexR_ = -(Size - IndexR) + 1
            result += lst[0] + IndexR_
        else : 
            IndexR_ = -(Size - IndexR) + 1
            result += lst[0] - IndexR_
    
print(result)