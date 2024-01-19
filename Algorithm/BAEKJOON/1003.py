def callzero() :
    global zero
    zero += 1

def callone() :
    global one
    one += 1

def fibonacci(n) :
    global zero, one, fib, lst
    
    if n < 0 :
        return
    if fib[n] != -1 :
        lst[0] += fib[n][0]
        lst[1] += fib[n][1]
        return
    
    if n == 0 :
        callzero()
    if n == 1 :
        callone()
    if n > 1 :
        fibonacci(n-1)
        fibonacci(n-2)
    
    lst[0] += zero
    lst[1] += one
    fib[n] = lst.copy()

result = []
fib = [-1 for _ in range(41)]
for i in range(41) :
    zero = 0
    one = 0
    lst = [0, 0]
    fibonacci(i)
    
N = int(input())
result = []
for _ in range(N) :
    result.append(fib[int(input())])

for num in result :
    print(num[0], num[1])