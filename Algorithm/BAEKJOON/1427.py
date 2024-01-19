N = input()
arr = []
for i in N :
    arr.append(int(i))

arr.sort(reverse=True)
arr = "".join(list(map(str, arr)))
print(arr)