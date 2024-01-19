N = int(input())
count = 1

while N >= count :
    N -= count
    count += 1
    
print(count - 1)