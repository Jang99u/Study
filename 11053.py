SIZE = int(input(""))
N = list(map(int, input("").split()))

length = []
for i in range(SIZE) :
    length.append(0)

for i in range(SIZE) :
    length[i] = 1
    for j in range(i) :
        if N[i] > N[j] :
            length[i] = max(length[i], length[j] + 1)
            
print(max(length))