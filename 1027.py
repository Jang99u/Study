HowManyBuilding = int(input(""))
BuildingHeight = list(map(int, input("").split()))
CanWatchBuilding = []

for i in range(HowManyBuilding) :
    GoLeft = i
    GoRight = HowManyBuilding - (i + 1)
    HowManyWatch = 0 
    
    MinHeightRatio = 1000000000
    for j in range(GoLeft) :
        j += 1
        Building = i
        LeftBuilding = i - j
        if BuildingHeight[LeftBuilding] > BuildingHeight[Building] - MinHeightRatio * j :
            HowManyWatch += 1
        HeightRatio = (BuildingHeight[Building] - BuildingHeight[LeftBuilding]) / j
        MinHeightRatio = min(MinHeightRatio, HeightRatio)
    
    MaxHeightRatio = -1000000000
    for k in range(GoRight) :
        k += 1
        Building = i
        RightBuilding = i + k
        if BuildingHeight[Building] + MaxHeightRatio * k < BuildingHeight[RightBuilding] :
            HowManyWatch += 1
        HeightRatio = (BuildingHeight[RightBuilding] - BuildingHeight[Building]) / k
        MaxHeightRatio = max(MaxHeightRatio, HeightRatio)
        
    CanWatchBuilding.append(HowManyWatch)
    
print(max(CanWatchBuilding))