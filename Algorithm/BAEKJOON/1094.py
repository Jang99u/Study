N = int(input())
num = [64, 32, 16, 8, 4, 2, 1]

B = 0
for i in num :
    if i <= N :
        N -= i
        B += 1
    if N == 0 :
        break
print(B)