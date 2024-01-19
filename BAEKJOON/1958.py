X = input()
Y = input()
Z = input()

arr = [[[0 for _ in range(len(X)+1)] for _ in range(len(Y)+1)] for _ in range(len(Z)+1)]

for i in range(len(X)) :
    for j in range(len(Y)) :
        for k in range(len(Z)) :
            if Z[k] == Y[j] and Z[k] == X[i] :
                arr[k+1][j+1][i+1] = arr[k][j][i] + 1
            else :
                arr[k+1][j+1][i+1] = max(arr[k][j+1][i+1], arr[k+1][j][i+1], arr[k+1][j+1][i])
                
print(arr[len(Z)][len(Y)][len(X)])