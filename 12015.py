def BinarySearch(num) :
    global lst
    start = 0
    end = len(lst)
    
    while start < end :
        mid = (start + end) // 2
        if num > lst[mid] :
            start = mid + 1
        else :
            end = mid
            
    lst[end] = num

SIZE = int(input(""))
N = list(map(int, input("").split()))

lst = []
for i in range(SIZE) :
    if i == 0 :
        lst.append(N[i])
        continue
    
    if N[i] > lst[-1] :
        lst.append(N[i])
        continue
    else :
        BinarySearch(N[i])
    
print(len(lst))