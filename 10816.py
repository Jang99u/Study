NSIZE = int(input(""))
N = list(map(int, input("").split()))

Card = {}
for i in range(NSIZE) :
    try :
        Card[N[i]] += 1
    except :
        Card[N[i]] = 1


MSIZE = int(input("")) 
M = list(map(int, input("").split()))
for i in range(MSIZE - 1) :
    try :
        print(Card[M[i]], end= " ")
    except :
        print(0, end=" ")
        
try :
    print(Card[M[-1]])
except :
    print(0)