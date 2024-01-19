arr = [1, 2, 4]

for i in range(3, 10) :
    sum = arr[i-3] + arr[i-2] + arr[i-1]
    arr.append(sum)

N = int(input())
for _ in range(N) :
    print(arr[int(input())-1])