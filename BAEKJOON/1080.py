def IsNotSameNum(num_1, num_2) :
    if num_1 != num_2 :
        return True
    else : 
        return False
    
def IsSameArr(arr_1, arr_2) :
    global size_r, size_c
    IsSameArr_ = True
    for i in range(size_r) :
        for j in range(size_c) :
            if IsNotSameNum(arr_1[i][j], arr_2[i][j]) : 
                IsSameArr_ = False
                break
    return IsSameArr_                   
    
def IsSizeFalse(rsize, csize) :
    if rsize < 3 or csize < 3 :
        return True
    else :
        return False
    
def ReverseNum(r, c) :
    global arr_check
    for i in range(3) :
        i += r
        for j in range(3) :
            j += c
            if arr_check[i][j] == 1 :
                arr_check[i][j] = 0
            else :
                arr_check[i][j] = 1

size = input("")
size = size.split()
size_r = int(size[0])
size_c = int(size[1])

arr_check = []
arr_change = []

for i in range(size_r) :
    lst = []
    input_num = input("")
    for j in range(size_c) :
        lst.append(int(input_num[j]))
    arr_check.append(lst)
for i in range(size_r) :
    lst = []
    input_num = input("")
    for j in range(size_c) :
        lst.append(int(input_num[j]))
    arr_change.append(lst)

if IsSizeFalse(size_r, size_c) :
    if IsSameArr(arr_check, arr_change) :
        print(0)
        exit(0)
    else :
        print(-1)
        exit(0)

count = 0
for i in range(size_r-2) :
    for j in range(size_c-2) :
        if IsNotSameNum(arr_check[i][j], arr_change[i][j]) :
            ReverseNum(i, j)
            count += 1
            
if IsSameArr(arr_check, arr_change) :
    print(count)
else :
    print(-1)