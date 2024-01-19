import re

N = list(map(int, input("").split()))
HowManyMaterial = N[0]
HowManyFormula = N[1]

MaterialCost_lst = {}
for i in range(HowManyMaterial) :
    N = input("").split()
    N[1] = int(N[1])
    MaterialCost_lst[N[0]] = N[1]
MaterialCost_lst = dict(sorted(MaterialCost_lst.items(), key=lambda x:x[1]))
    
Compound_lst = []
Formula_lst = []
for i in range(HowManyFormula) :
    N = input("")
    Compound = re.findall("([A-Z]{0,})=", N)
    N = re.sub("[A-Z]{0,}=", "", N)
    N = re.split("\+", N)
    Compound_lst.append(Compound)
    Formula_lst.append(N)

count = 0
while 1 :
    if count == len(MaterialCost_lst.keys()) :
        break
    
    N = list(MaterialCost_lst.keys())[count]
    for i in range(len(Formula_lst)) :
        for j in range(len(Formula_lst[i])) :
            try :
                if N == Formula_lst[i][j][1:] :
                    Formula_lst[i][j] = int(Formula_lst[i][j][0]) * MaterialCost_lst[Formula_lst[i][j][1:]]
            except :
                continue

    for i in range(HowManyFormula) :
        try :
            Formula_lst[i][0] = int(Formula_lst[i][0])
            Formula_lst[i] = [sum(Formula_lst[i])]
            if Compound_lst[i][0] not in MaterialCost_lst.keys() :
                MaterialCost_lst[Compound_lst[i][0]] = Formula_lst[i][0]
            else :
                MaterialCost_lst[Compound_lst[i][0]] = min(MaterialCost_lst[Compound_lst[i][0]], Formula_lst[i][0])
        except :
            continue
        
    MaterialCost_lst = dict(sorted(MaterialCost_lst.items(), key=lambda x:x[1]))    
    count += 1

try :
    if MaterialCost_lst["LOVE"] > 1000000000 :
        print(1000000001)
    else :
        print(MaterialCost_lst["LOVE"])
except :
    print(-1)