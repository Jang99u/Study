while True :
    N = input()
    if N == '.' :
        break
    
    stack = []
    CanBalance = True
    for i in N :
        if i == '(' or i == '[' :
            stack.append(i)
        if i == ')' :
            if len(stack) == 0 or stack.pop() != '(' :
                print("no")
                CanBalance = False
                break
        if i == ']' :
            if len(stack) == 0 or stack.pop() != '[' :
                print("no")
                CanBalance = False
                break
    
    if CanBalance == False :
        pass
    else :
        if len(stack) != 0 :
            print("no")
        else :
            print("yes")