r, c = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(r)]

def IsRectangle(n, size) :
    size -= 1
    for i in range(r-size) :
        for j in range(c-size) :
            if arr[i][j] == n and arr[i+size][j] == n and arr[i][j+size] == n and arr[i+size][j+size] == n :
                return True
    return False

size = min(r, c)
while size > 1 :
    for i in range(10) :
        if IsRectangle(i, size) :
            print(size*size)
            exit()
    size -= 1
print(1)