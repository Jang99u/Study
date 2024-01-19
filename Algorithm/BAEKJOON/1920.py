SIZE = int(input(""))
SETNUM = set(map(int, input("").split()))
NUM = int(input(""))
MYNUM = list(map(int, input("").split()))

for i in range(NUM) :
    if MYNUM[i] in SETNUM :
        print(1)
    else :
        print(0)