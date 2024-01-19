import sys

def find(num) :
    global dic, dic_
    
    if num not in dic :
        return []
    
    if num in dic_ :
        return dic_[num]
    elif num not in dic_ :
        result = list(dic[num])
        for i in dic[num] :
            result += find(i)
        result = set(result)
        dic_[num] = result
        return dic_[num]

N = list(map(int, sys.stdin.readline().rstrip().split()))
CaseCompare = N[1]
dic_ = {}

lst = []
for i in range(CaseCompare) :
    N = list(map(int, sys.stdin.readline().rstrip().split()))
    lst.append(N)
lst.sort()

dic = {}
for i in range(CaseCompare) :
    try :
        dic[lst[i][0]].add(lst[i][1])
    except :
        dic[lst[i][0]] = set([lst[i][1]])    

for i in dic :
    find(i)

T = int(input(""))
lst_ = []
for _ in range(T) :
    N = list(map(int, input("").split()))
    lst_.extend(N)
    
result_ = []
for i in range(T) :
    front = lst_[2*i]
    end = lst_[2*i+1]
    
    if front in dic_ and end in dic_[front] :
        result_.append('-1')
    elif end in dic_ and front in dic_[end] :
        result_.append('1')
    else :
        result_.append('0')
        
print('\n'.join(result_))