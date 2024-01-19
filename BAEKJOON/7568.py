import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N) :
    lst.append(list(map(int, input().split())))

rank = []
for i in lst :
    r = 0
    for j in lst :
        if i[0] < j[0] and i[1] < j[1] :
            r += 1
    rank.append(str(r+1))
print(" ".join(rank))