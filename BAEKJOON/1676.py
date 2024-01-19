N = int(input())

result = 1
count = 0
for i in range(N) :
    i += 1
    result *= i
    
    if result % 10 == 0 :
        while result % 10 == 0 :
            result //= 10
            count += 1

print(count)