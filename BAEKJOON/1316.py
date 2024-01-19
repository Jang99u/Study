N = int(input())

result = 0
for _ in range(N) :
    word = input()
    cnt = word[0]
    wordset = set([word[0]])
    IsGroup = True
    
    for i in range(len(word)) :
        if word[i] == cnt :
            continue
        else :
            if word[i] in wordset :
                IsGroup = False
                break
            wordset.add(word[i])
        cnt = word[i]
    if IsGroup :
        result += 1
        
print(result)