import copy
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
node = []
chiken = []
for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            node.append([i, j])
        if city[i][j] == 2 :
            chiken.append([i, j])
chiken_ = list(combinations(chiken, len(chiken)-M))

result = 1000000
for lst in chiken_ :
    count = 0
    c = copy.deepcopy(chiken)
    for i in lst :
        c.remove(i)
    for i, j in node :
        cnt = 1000000
        for i_, j_ in c :
            cnt = min(cnt, abs(i_-i) + abs(j_-j))
        count += cnt
    result = min(result, count)
        
print(result)