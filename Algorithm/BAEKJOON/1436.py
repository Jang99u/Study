N = int(input())

num = 1
cnt = 0
while 1 :
    if "666" in str(num) :
       cnt += 1 
    if cnt == N :
        break
    num += 1

print(num)