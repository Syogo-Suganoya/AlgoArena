N = int(input())
WX = [list(map(int, input().split())) for _ in range(N)]

res = 0

for i in range(N):
    tmp = WX[i][0]  # i の仕事は必ず含める
    for j in range(N):
        if i == j:
            continue
        # i→j に向かうときの時間差
        diff = (WX[j][1] - WX[i][1]) % 24
        if 0 <= diff <= 8:
            tmp += WX[j][0]
    res = max(res, tmp)

print(res)
