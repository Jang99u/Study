N = int(input())
dic = {}

for _ in range(N) :
    book = input()
    if book not in dic :
        dic[book] = 1
    else :
        dic[book] += 1

cnt = 0
result = "."
for i in list(dic.keys()) :
    if dic[i] > cnt :
        cnt = dic[i]
        result = i
    elif dic[i] == cnt :
        lst = [result, i]
        lst.sort()
        result = lst[0]
print(result)