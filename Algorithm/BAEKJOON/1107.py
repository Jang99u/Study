def IsNotContain(check_lst) :
    global CanUse
    IsNotContain_ = False
    for i in range(len(check_lst)) :
        if check_lst[i] not in CanUse :
            IsNotContain_ = True
            break
    return IsNotContain_

def Makelst(num) :
    num = str(num)
    num_lst = []
    for i in range(len(num)) :
        num_lst.append(int(num[i]))
    return num_lst
    
def GoUp(num) :
    GoNext = num + 1
    GoNext = Makelst(GoNext)
    if IsNotContain(GoNext) == False :
        return -1
    else : 
        return num + 1
    
def GoDown(num) :
    if num <= 0 :
        return 0
    GoNext = num - 1
    GoNext = Makelst(GoNext)
    if IsNotContain(GoNext) == False :
        return -1
    else : 
        return num - 1

target_num = int(input(""))
target_num = Makelst(target_num)
CheckCount = 0
StartChannel = 100
CanUse = [0,1,2,3,4,5,6,7,8,9]

HowManyError = int(input(""))
if HowManyError != 0 :
    WhatError = input("")
    WhatError = WhatError.split()
    for i in range(len(WhatError)) :
        a = int(WhatError[i])
        CanUse[a] = -1
    
target_num = "".join(map(str, target_num))
target_num = int(target_num)
num_up = target_num
num_down = target_num
    
while 1 :
    
    Channel_Difference = StartChannel - target_num
    if Channel_Difference < 0 :
        Channel_Difference = -Channel_Difference
    if Channel_Difference < CheckCount :
        GoNum = 500000
        break
    
    if HowManyError == 0 or IsNotContain(Makelst(target_num)) == False :
        if Channel_Difference < len(str(target_num)) :
            GoNum = 500000
            break
        GoNum = len(str(target_num))
        break
  
    if GoDown(num_down) == -1 :
        GoNum = num_down - 1
        len_1 = len(str(GoNum))
        GoNum = len_1
        if GoUp(num_up) == -1 :
            GoNum = num_up
            len_2 = len(str(GoNum))
            GoNum = min(len_1, len_2)
        CheckCount += 1  
        break 
    
    if GoUp(num_up) == -1 :
        GoNum = num_up + 1
        len_1 = len(str(GoNum))
        GoNum = len_1
        if GoDown(num_down) == -1 :
            GoNum = num_down
            len_2 = len(str(GoNum))
            GoNum = min(len_1, len_2)
        CheckCount += 1  
        break 
    
    num_up = GoUp(num_up)
    num_down = GoDown(num_down)
    CheckCount += 1  

result = GoNum + CheckCount
if Channel_Difference < result :
    result = Channel_Difference
print(result)