N = list(map(int, input("").split()))
M = N[1]
N = N[0]

dic = {}
for i in range(N) :
    Name = input("")
    dic[Name] = Name

lst = []
for i in range(M) :
    Name = input("")
    try :
        lst.append(dic[Name])
    except :
        continue
lst.sort()

print(len(lst))
for i in range(len(lst)) :
    print(lst[i])