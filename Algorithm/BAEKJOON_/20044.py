Team = int(input(""))
N = list(map(int, input("").split())).sort()

result = []
for i in range(Team) :
    Score = N[i] + N[-(i+1)]
    result.append(Score)

print(min(result))