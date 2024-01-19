# Array Shift Operation Error

class Wheel :
    def __init__(self, WheelNum, WheelShape) :
        self.WheelNum = WheelNum
        self.WheelShape = WheelShape
        
    def Rotate(self, direction) :
        if direction == 1 :
            num = self.WheelShape[7]
            for i in range(7) :
                i = 7-i
                self.WheelShape[i] = self.WheelShape[i-1]
            self.WheelShape[0] = num

        elif direction == -1 :
            num = self.WheelShape[0]
            for i in range(7) :
                self.WheelShape[i] = self.WheelShape[i+1]
            self.WheelShape[7] = num
    
    def NextRotateNum(self) :
        NextRotate = []
        global HowManyWheel
        if self.WheelNum == 1 :
            NextRotate.append(2)
        elif self.WheelNum == HowManyWheel :
            NextRotate.append(HowManyWheel-1)
        else :
            NextRotate.append(self.WheelNum-1)
            NextRotate.append(self.WheelNum+1)
        
        return NextRotate

def Rotate_(WhatWheelRotate, NextRotate, StartDirection) :
    global Wheel_lst
    global HowManyWheel
    LEFT = 6
    RIGHT = 2
    WhatWheelRotate_LEFT = WhatWheelRotate
    WhatWheelRotate_RIGHT = WhatWheelRotate
    
    for i in range(len(NextRotate)) :
        if Wheel_lst[NextRotate[i]].WheelNum < Wheel_lst[WhatWheelRotate].WheelNum :
            GoLeft_1 = NextRotate[i]
            GoLeft_2 = WhatWheelRotate
            HowManyGoLeft = 0
            RotateDirection = StartDirection
            
            while 1 :
                compare = Wheel_lst[GoLeft_1].WheelShape[RIGHT] != Wheel_lst[GoLeft_2].WheelShape[LEFT]
                if compare == False :
                    break
                HowManyGoLeft += 1
                if GoLeft_1 == 1 :
                    break
                GoLeft_1 -= 1
                GoLeft_2 -= 1
            
            for i in range(HowManyGoLeft) :
                WhatWheelRotate_LEFT -= 1
                RotateDirection = -RotateDirection
                Wheel_lst[WhatWheelRotate_LEFT].Rotate(RotateDirection)

        elif Wheel_lst[NextRotate[i]].WheelNum > Wheel_lst[WhatWheelRotate].WheelNum :
            GoRight_1 = NextRotate[i]
            GoRight_2 = WhatWheelRotate
            HowManyGoRight = 0
            RotateDirection = StartDirection
            
            while 1 :
                compare = Wheel_lst[GoRight_1].WheelShape[LEFT] != Wheel_lst[GoRight_2].WheelShape[RIGHT]
                if compare == False :
                    break
                HowManyGoRight += 1
                if GoRight_1 == HowManyWheel :
                    break
                GoRight_1 += 1
                GoRight_2 += 1

            for i in range(HowManyGoRight) :
                WhatWheelRotate_RIGHT += 1
                RotateDirection = -RotateDirection
                Wheel_lst[WhatWheelRotate_RIGHT].Rotate(RotateDirection)
    Wheel_lst[WhatWheelRotate].Rotate(StartDirection)

HowManyWheel = int(input(""))
Wheel_lst = []
Wheel_lst.append(0)
for i in range(HowManyWheel) :
    lst = []
    WhatWheel = input("")
    for j in range(len(WhatWheel)) :
        lst.append(int(WhatWheel[j]))
    obj = Wheel((i + 1), lst)
    Wheel_lst.append(obj)


HowManyRotate = int(input(""))
for i in range(HowManyRotate) :
    NumInput = input("")
    NumInput = NumInput.split()
    WhatWheelRotate = int(NumInput[0])
    RotateDirection = int(NumInput[1])
    NextRotate = Wheel_lst[WhatWheelRotate].NextRotateNum()
    Rotate_(WhatWheelRotate, NextRotate, RotateDirection)  

result = 0
for i in range(HowManyWheel + 1) :
    if i == 0 :
        continue
    if Wheel_lst[i].WheelShape[0] == 1 :
        result += 1
print(result)