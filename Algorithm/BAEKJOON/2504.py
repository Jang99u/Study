def Check() :
    global lst
    
    Stack = []
    for i in lst :
        Stack.append(i)
        if i == ')' :
            Stack.pop()
            try :
                N = Stack.pop()
                if N != '(' :
                    exit(0)
            except :
                print(0)
                exit(0)
        if i == ']' :
            Stack.pop()
            try :
                N = Stack.pop()
                if N != '[' :
                    exit(0)
            except :
                print(0)
                exit(0)
    if len(Stack) != 0 :
        print(0)
        exit(0)

def FindIndex1(i) :
    global Stack
    if i == 0 :
        return -1
    if i > 0 and Stack[i-1] == '(' :
        return i-1
    if i > 0 and Stack[i-1] != '(' :
        result = FindIndex1(i-1)
        return result
    
def FindIndex2(i) :
    global Stack
    if i == 0 :
        return -1
    if i > 0 and Stack[i-1] == '[' :
        return i-1
    if i > 0 and Stack[i-1] != '[' :
        result = FindIndex2(i-1)
        return result
    
def StackSort() :
    global Stack, lst
    
    for i in range(len(lst)) :
        Stack.append(lst[i])
        
        if lst[i] == ')' :
            Index1 = FindIndex1(i)
            if Index1 == -1 :
                print(0)
                exit(0)
            if i - Index1 == 1 :
                Stack.pop()
                Stack.pop()
                Stack.append(2)
                Stack.append('-')
            else : 
                result = 0
                count = 0
                Calculate = True
                for j in range(Index1+1, i) :
                    if type(Stack[j]) == int :
                        result += Stack[j]
                        count += 1
                    elif Stack[j] == '-' :
                        count += 1
                        continue
                    else :
                        Calculate = False
                        break
                if Calculate == True :
                    for _ in range(count) :
                        Stack.pop()
                    Stack.pop()
                    Stack.pop()
                    Stack.append(result*2)
                    Stack.append('-')
                    for _ in range(count) :
                        Stack.append('-')
                
        if lst[i] == ']' :
            Index2 = FindIndex2(i)
            if Index2 == -1 :
                print(0)
                exit(0)
            if i - Index2 == 1 :
                Stack.pop()
                Stack.pop()
                Stack.append(3)
                Stack.append('-')
            else : 
                result = 0
                count = 0
                Calculate = True
                for j in range(Index2+1, i) :
                    if type(Stack[j]) == int :
                        result += Stack[j]
                        count += 1
                    elif Stack[j] == '-' :
                        count += 1
                        continue
                    else :
                        Calculate = False
                        break
                if Calculate == True :
                    for _ in range(count) :
                        Stack.pop()
                    Stack.pop()
                    Stack.pop()
                    Stack.append(result*3)
                    Stack.append('-')
                    for _ in range(count) :
                        Stack.append('-')
                
    remove_set = {'-'}
    lst = [i for i in Stack if i not in remove_set]
    return lst

N = input()
lst = []
for i in N :
    lst.append(i)
Check()

while '(' in lst or ')' in lst or '[' in lst or ']' in lst :
    Stack = []
    lst = StackSort()

print(sum(lst))