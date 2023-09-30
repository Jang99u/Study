N = int(input())
arr = [list(input()) for _ in range(N)]
word = {}
for i in range(N) :
    for j in range(N) :
        if arr[i][j] != '.' and arr[i][j] not in word :
            word[arr[i][j]] = [i, j]

def slope(p, q, r) :
    if p == q or p == r or q == r :
        return False
    if p not in word or q not in word or r not in word :
        return False
    if word[p][0] - word[q][0] == 0 or word[p][0] - word[r][0] == 0 :
        if word[p][0] - word[q][0] == 0 and word[p][0] - word[r][0] == 0 :
            return True
        else :
            return False
    
    s1 = (word[p][1] - word[q][1]) / (word[p][0] - word[q][0])
    s2 = (word[p][1] - word[r][1]) / (word[p][0] - word[r][0])
    if s1 == s2 :
        return True
    else :
        return False

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
result = []
for i in alphabet :
    for j in alphabet :
        for k in alphabet :
            if slope(i, j, k) :
                if set([i, j, k]) not in result :
                    result.append(set([i, j, k]))
print(len(result))