D, N = map(int, input().split())

oven = list(map(int, input().split()))
piza = list(map(int, input().split()))

for i in range(1, len(oven)) :
    if oven[i] > oven[i-1] :
        oven[i] = oven[i-1]

for i in range(len(piza)) :
    if len(oven) != 0 :
        M = oven.pop()
    else :
        print(0)
        exit()
    while piza[i] > M :
        if len(oven) != 0 :
            M = oven.pop()
        else :
            print(0)
            exit()
print(len(oven)+1)