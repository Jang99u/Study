N = int(input())

lst = []
for _ in range(N) :
    S, E = map(int, input().split())
    lst.append([S, E])
lst = sorted(lst, key = lambda x : x[1])

lst_ = []
res = []
endtime = lst[0][1]
for i in lst :
    if i[1] != endtime :
        res.extend(sorted(lst_, key = lambda x : x[0]))
        lst_ = []
    lst_.append(i) 
    endtime = i[1]
res.extend(sorted(lst_, key = lambda x : x[0]))

result = [res[0]]
for i in res[1:] :
    T = result[-1][1]
    if i[0] >= T :
        result.append(i)
        
print(len(result))