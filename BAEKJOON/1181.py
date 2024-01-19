N = int(input(""))

word = set([])
for i in range(N) :
    W = input("")
    word.add(W)

word = sorted(word, key=lambda x: len(x))
print(word)

lst = []
result = []
for i in range(N) :
    pass