import sys
from math import sqrt

TC = int(input())

result = []
for _ in range(TC) :
    startx, starty, endx, endy = map(int, sys.stdin.readline().split())
    planet = int(input())
    move = 0
    for _ in range(planet) :
        px, py, r = map(int, sys.stdin.readline().split())
        distanceS = abs(sqrt((px-startx)**2 + (py-starty)**2))
        distanceE = abs(sqrt((px-endx)**2 + (py-endy)**2))
        if distanceS < r or distanceE < r :
            move += 1
        if distanceS < r and distanceE < r :
            move -= 1
    result.append(move)
    
for i in result :
    print(i)

# Å×½ºÆ®