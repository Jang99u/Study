Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AlphabetDic = {}
for i in Alphabet :
    AlphabetDic[i] = 0
    
N = input("")
lst = []
for i in N :
    AlphabetDic[i] += 1
    lst.append(0)
    
count = 0
index = 0
for i in Alphabet :
    if AlphabetDic[i] % 2 != 0 :
        index = i
        count += 1
if count > 1 :
    print("I'm Sorry Hansoo")
    exit(0)
if index != 0 :
    lst[len(lst)//2] = index
    
input = 0
input_reverse = -1
for i in Alphabet :
    for j in range(AlphabetDic[i]//2) :
        lst[input] = i
        lst[input_reverse] = i
        input += 1
        input_reverse -= 1
        
print("".join(lst))