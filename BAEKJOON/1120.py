X, Y = input().split()

result = 100000
for i in range(len(Y)-len(X)+1) :
    cnt = 0
    for j in range(len(X)) :
        if X[j] != Y[i+j] :
            cnt += 1
    if cnt <= result :
        result = cnt

print(result)