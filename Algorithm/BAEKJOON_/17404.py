N = int(input())
INF = 1000000

rgb = []
for _ in range(N) :
    rgb.append(list(map(int, input().split())))

dp1 = [[INF, rgb[0][0] + rgb[1][1], rgb[0][0] + rgb[1][2]]]
dp2 = [[rgb[0][1] + rgb[1][0], INF, rgb[0][1] + rgb[1][2]]]
dp3 = [[rgb[0][2] + rgb[1][0], rgb[0][2] + rgb[1][1], INF]]

for i in range(N) :
    if i == 0 or i == 1:
        continue
    i -= 1
    cnt1 = [
        min(dp1[i-1][1] + rgb[i+1][0], dp1[i-1][2] + rgb[i+1][0]),
        min(dp1[i-1][0] + rgb[i+1][1], dp1[i-1][2] + rgb[i+1][1]),
        min(dp1[i-1][0] + rgb[i+1][2], dp1[i-1][1] + rgb[i+1][2])
        ]
    dp1.append(cnt1)
    cnt2 = [
        min(dp2[i-1][1] + rgb[i+1][0], dp2[i-1][2] + rgb[i+1][0]),
        min(dp2[i-1][0] + rgb[i+1][1], dp2[i-1][2] + rgb[i+1][1]),
        min(dp2[i-1][0] + rgb[i+1][2], dp2[i-1][1] + rgb[i+1][2])
        ]
    dp2.append(cnt2)
    cnt3 = [
        min(dp3[i-1][1] + rgb[i+1][0], dp3[i-1][2] + rgb[i+1][0]),
        min(dp3[i-1][0] + rgb[i+1][1], dp3[i-1][2] + rgb[i+1][1]),
        min(dp3[i-1][0] + rgb[i+1][2], dp3[i-1][1] + rgb[i+1][2])
        ]
    dp3.append(cnt3)
    
print(min(dp1[-1][1], dp1[-1][2], dp2[-1][0], dp2[-1][2], dp3[-1][0], dp3[-1][1]))