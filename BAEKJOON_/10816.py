NSIZE = int(input(""))
N = list(map(int, input("").split()))

Card = {}
for i in range(NSIZE) :
    if N[i] not in Card.keys() :
        Card[N[i]] = 1
    else :
        Card[N[i]] += 1

MSIZE = int(input("")) 
M = list(map(int, input("").split()))
for i in range(MSIZE) :
    if M[i] in Card.keys() :
        print(Card[M[i]], end= " ")
    else :
        print(0, end=" ")