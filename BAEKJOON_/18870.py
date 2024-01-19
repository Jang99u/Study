N = int(input())
lst = list(map(int, input().split()))
table = sorted(list(set(lst)), reverse=True)

dic = {}
for i in range(len(table)) :
    dic[table[i]] = len(table) - (i+1)
    
result = []
for num in lst :
    result.append(str(dic[num]))
print(" ".join(result))