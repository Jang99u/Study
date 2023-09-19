N = int(input())
lst = list(map(int, input().split()))
for i in range(len(lst)) :
    lst[i] = [lst[i], i]    
lst = sorted(lst, key = lambda x : x[0])
for i in range(len(lst)) :
    lst[i].append(i)
lst = sorted(lst, key = lambda x : x[1])

for i in lst :
    print(i[2], end = " ")