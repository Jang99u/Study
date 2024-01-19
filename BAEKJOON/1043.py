def Know_(lst) :
    global HwoKnow, KnowTrue
    for i in range(len(lst)) :
        if HwoKnow[lst[i] - 1][1] == False :
            HwoKnow[lst[i] - 1] = [lst[i] , True]
            KnowTrue.append([lst[i] , True])

N = list(map(int, input("").split()))
HowManyPeople = N[0]
HowManyParty = N[1]
HwoKnow = []
HwoKnowTrue = []
for i in range(HowManyPeople) :
    i += 1
    HwoKnow.append([i, False])

N = list(map(int, input("").split()))
HowManyKnow = N[0]
if HowManyKnow != 0 :
    for i in range(HowManyKnow) :
        i += 1
        HwoKnow[N[i] - 1] = [N[i], True]
KnowTrue = list(filter(lambda x:x[1]==True, HwoKnow))

Party = []
for i in range(HowManyParty) :
    N = list(map(int, input("").split()))
    N = N[1:]
    Party.append(N)

for i in range(HowManyPeople) :
    if len(KnowTrue) == 0 :
        break
    for j in range(HowManyParty) :
        try :
            if KnowTrue[i][0] in Party[j] :
                Know_(Party[j])
        except :
            break

KnowResult = []
for i in range(len(KnowTrue)) :
    KnowResult.append(KnowTrue[i][0])
    
Result = 0
for i in range(HowManyParty) :
    CanLie = True
    for j in range(len(KnowResult)) :
        if KnowResult[j] in Party[i] :
            CanLie = False
    if CanLie :
        Result += 1

print (Result)