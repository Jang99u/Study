import sys
input = sys.stdin.readline

N = int(input())
if N == 0 :
    print(0)
    exit()
cut = round((N * 0.15)+0.0000001)

score = sorted([int(input()) for _ in range(N)])
score = score[cut:]
for _ in range(cut) :
    score.pop()
    
print(round((sum(score)/len(score))+0.0000001))