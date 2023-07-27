def BinarySearch(num) :
    global lst
    start = 0
    end = len(lst) - 1
    
    while 1 :
        mid = (start + end) // 2
        if num > lst[-1] :
            lst.append(num)
            return
        if start == end :
            end = mid
            break
        elif num == lst[mid] :
            return
        elif num > lst[mid] :
            start = mid + 1
        elif num < lst[mid] :
            end = mid
            
    lst[end] = num

SIZE = int(input(""))
N = list(map(int, input("").split()))

lst = []
for i in range(SIZE) :
    if i == 0 :
        lst.append(N[i])
        continue
    BinarySearch(N[i])
    
print(len(lst))