size = int(input(""))
arr_IsFriend = []
arr_HowManyFriend = []

for i in range(size) :
    line = []
    for j in range(size) :
        line.append(0)
    arr_IsFriend.append(line)

for i in range(size) :
    arr_HowManyFriend.append(0)

for i in range(size) :
    IsFriend = input("")
    for j in range(size) :
        if IsFriend[j] == 'N' :
            arr_IsFriend[i][j] = 0
        else :
            arr_IsFriend[i][j] = 1
            
for i in range(size) :
    for j in range(size) :
        if arr_IsFriend[i][j] == 1 :
            arr_HowManyFriend[i] += 1
        else :
            if i == j :
                continue
            for k in range(size) :
                if arr_IsFriend[i][k] == 1 and arr_IsFriend[i][k] == arr_IsFriend[k][j] :
                    arr_HowManyFriend[i] += 1
                    break

result = max(arr_HowManyFriend)
print(result)