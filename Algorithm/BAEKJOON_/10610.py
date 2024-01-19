num = list(map(int, list(input())))

if 0 not in num :
    print(-1)
    exit()
num.remove(0)
if sum(num) % 3 != 0 :
    print(-1)
    exit()
num.sort(reverse=True)
num = list(map(str, num))
print("".join(num) + "0")