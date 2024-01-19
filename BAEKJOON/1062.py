import re
from itertools import combinations

def Combinations(r) :
    return list(combinations("bdefghjklmopqrsuvwxyz", r))

pat = re.compile(r"[bd-hj-mo-su-z]")
word_set = []
N, K = map(int, input().split())
for _ in range(N) :
    word = re.findall(pat, input())
    word_set.append(set(word))

if K < 5 :
    print(0)
    exit(0)
else :
    K -= 5
    alph = Combinations(K)
    result = 0
    for i in alph :
        HowManySet = 0
        i = set(i)
        for j in word_set :
            if len(j - i) == 0 :
                HowManySet += 1
                
        result = max(result, HowManySet)

print(result) 