strnumlst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numlst = [0,1,2,3,4,5,6,7,8,9]
result = lst

while len(numlst) != 0 :
    inputlst = []
    for j in numlst :
        k = 0
        while lst[k][0] != str(j) :
            inputlst.append(strnumlst[j] + lst[k])
            k += 1
    result.extend(inputlst)
    lst = inputlst
    numlst.pop(0)

N = int(input())
N = N-1
try :
    print(int(result[N]))
except :
    print(-1)