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


# Memory Exceeded
'''
N = list(map(int, input("").split()))
row = N[0]
jump = N[1]

Arr = []
for i in range(row) :
    lst = []
    for j in range(row) :
        lst.append(0)
    Arr.append(lst)
    
for i in range(row) :
    if i == 0 :
        Arr[0][i] = 1
        Arr[row-1][-(i+1)] = row**2
    elif i % 2 != 0 :
        Arr[0][i] = Arr[0][i-1] + 1
        Arr[row-1][-(i+1)] = Arr[row-1][-i] - 1
    else : 
        Arr[0][i] = Arr[0][i-1] + 4*(i//2)
        Arr[row-1][-(i+1)] = Arr[row-1][-i] - 4*(i//2)

for i in range(row) :
    for j in range(i) :
        j += 1
        if i % 2 != 0 :
            Arr[j][i-j] = Arr[j-1][i-(j-1)] + 1
            Arr[(row-1)-j][(row-(i+1))+j] = Arr[(row-1)-(j-1)][(row-(i+1))+(j-1)] - 1
        else :
            Arr[j][i-j] = Arr[j-1][i-(j-1)] - 1
            Arr[(row-1)-j][(row-(i+1))+j] = Arr[(row-1)-(j-1)][(row-(i+1))+(j-1)] + 1

N = input("")
result = 1
indexR = 0
indexC = 0
for i in range(jump) :
    if N[i] == "U" :
        indexR -= 1
        result += Arr[indexR][indexC]
    if N[i] == "D" :
        indexR += 1
        result += Arr[indexR][indexC]
    if N[i] == "L" :
        indexC -= 1
        result += Arr[indexR][indexC]
    if N[i] == "R" :
        indexC += 1
        result += Arr[indexR][indexC]
print(result)
'''

# Timeout
'''
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
        for i in range(Index+1) :
            if i == 0 :
                lst.append(StartNum[Index])
            else :
                if Index % 2 != 0 :
                    lst.append(lst[i-1]+1)
                else : 
                    lst.append(lst[i-1]-1)
        result += lst[IndexR]
    
    elif Index >= Size :
        lst = []
        for i in range(ArrSize - Index) :
            if i == 0 :
                lst.append(StartNum[Index])
            else :
                if Index % 2 != 0 :
                    lst.append(lst[i-1]-1)
                else : 
                    lst.append(lst[i-1]+1)
        lst.reverse()
        IndexR_ = -(Size - IndexR)
        result += lst[IndexR_]
    
print(result)
'''