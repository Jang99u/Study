N = int(input())

C = 0
while N > 0 :
    if N % 5 == 0 :
        N -= 5
        C += 1
    else :
        N -= 3
        C += 1

if N != 0 :
    print(-1)
else :
    print(C)