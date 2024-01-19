import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N) :
    log = input().split()
    if log[1] == "enter" :
        dic[log[0]] = True
    else :
        dic[log[0]] = False

result = []
for i in dic :
    if dic[i] == True :
        result.append(i)
result.sort(reverse=True)
print("\n".join(result))