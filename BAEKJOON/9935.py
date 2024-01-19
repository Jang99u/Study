def STRBOMB() :
    global Stack, BOMB
    
    lst = []
    for i in range(len(BOMB)) :
        i += 1
        
        POP = Stack.pop()
        lst.append(POP)
        if POP == BOMB[-i] :
            if len(Stack) == 0 and i != len(BOMB) : 
                for _ in range(len(lst)) :
                    Stack.append(lst.pop())
                break
                        
        if POP != BOMB[-i] :
            for _ in range(len(lst)) :
                Stack.append(lst.pop())
            break
    
N = input()
BOMB = input()

Stack = []
for i in N :
    Stack.append(i)
    POP = Stack.pop()
    Stack.append(POP)
    
    if POP == BOMB[-1] :
        STRBOMB()

if len(Stack) == 0 :
    print("FRULA")
else :
    print("".join(Stack))