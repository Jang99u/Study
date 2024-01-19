import sys
input = sys.stdin.readline

TC = int(input())
result = []
for _ in range(TC) :
    N = input().rstrip()
    stack = []
    VPS = "YES"
    for i in N :
        stack.append(i)
        if i == ')' :
            stack.pop()
            if len(stack) == 0 :
                VPS = "NO"
                break
            else : 
                if stack.pop() != '(' :
                    VPS = "NO"
                    break
    if len(stack) != 0 :
        VPS = "NO"
    result.append(VPS)

print("\n".join(result))