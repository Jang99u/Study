import sys
input = sys.stdin.readline

N = int(input())
dic = {}

for _ in range(N) :
    card = int(input())
    if card not in dic :
        dic[card] = 1
    else :
        dic[card] += 1

cnt = dic[list(dic.keys())[0]]
card = list(dic.keys())[0]
for i in dic :
    if dic[i] > cnt :
        cnt = dic[i]
        card = i
    elif dic[i] == cnt and i < card :
        cnt = dic[i]
        card = i
print(card)