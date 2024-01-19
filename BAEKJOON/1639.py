N = list(map(int, list(input())))
result = 0
strlen = 2

while strlen <= len(N) :
    for i in range(len(N) - strlen + 1) :
        if sum(N[i:i+(strlen//2)]) == sum(N[i+(strlen//2):i+strlen]) :
            result = strlen
            break
    strlen += 2
print(result)