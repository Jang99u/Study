def NewStack(i) :
    global stack, N, Alp, Operator1, Operator2, visited
    
    lst = []
    for j in range(i+1, len(N)) :
        if visited[j] == True : 
            continue
        
        if N[j] == ")" :
            visited[j] = True
            break
        
        if N[j] in Alp :
            visited[j] = True
            print(N[j], end="")
        elif N[j] in Operator1 :
            visited[j] = True
            if len(lst) != 0 :
                while lst[-1] not in Operator2 :
                    print(lst.pop(), end="")
                    if len(lst) == 0 :
                        break
            lst.append(N[j])
        elif N[j] in Operator2 :
            visited[j] = True
            while len(lst) != 0 :
                print(lst.pop(), end="")
            lst.append(N[j])
        
        if N[j] == "(" :
            visited[j] = True
            NewStack(j)
            
    while len(lst) != 0 :
        print(lst.pop(), end="")


N = input()
visited = [False for _ in range(len(N))]
Alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Operator1 = "*/"
Operator2 = "+-"

stack = []
index = 0
for i in range(len(N)) :
    if visited[i] == True :
        continue
    
    if N[i] in Alp :
        visited[i] = True 
        print(N[i], end="")
    elif N[i] in Operator1 :
        visited[i] = True
        if len(stack) != 0 :
            while stack[-1] not in Operator2 :
                print(stack.pop(), end="")
                if len(stack) == 0 :
                    break
        stack.append(N[i])
    elif N[i] in Operator2 :
        visited[i] = True
        while len(stack) != 0 :
            print(stack.pop(), end="")
        stack.append(N[i])

    if N[i] == "(" :
        visited[i] = True 
        NewStack(i)

while len(stack) != 0 :
    print(stack.pop(), end="")
