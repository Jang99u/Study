import sys
input = sys.stdin.readline

def BuyString(num, cost) :
    global lst1, lst6
    if num >= 6 :
        return num-6, cost+lst6[0][0]
    else : 
        if num*lst1[0][1] <= lst6[0][0] :
            return 0, cost+(num*lst1[0][1])
        else :
            return 0, cost+lst6[0][0]

N, M = map(int, input().split())
store = []

for i in range(M) :
    store.append(list(map(int, input().split())))
    
lst6 = sorted(store, key = lambda x : x[0]) # 6개 가격 기준 정렬
lst1 = sorted(store, key = lambda x : x[1]) # 1개 가격 기준 정렬
# 정렬 후 리스트로 끌고 다니지 말고 6개 기준 가장 싼 가격 / 1개 기준 가장 싼 가격 이렇게 2개만 필요함

if lst1[0][1] * 6 <= lst6[0][0] :
    print(lst1[0][1] * N)
    exit(0)
else :
    C = 0
    while N > 0 :
        N, C = BuyString(N, C)

print(C)