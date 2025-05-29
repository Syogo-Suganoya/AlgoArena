import math

D = int(input())
INF = float("inf")
res = INF

for i in range(int(math.sqrt(D)) + 1):
    a = i * i
    b = D - a
    if b < 0:
        continue
    # jの候補は、sqrt(b)とsqrt(b)+1の2つを確認
    j = int(math.sqrt(b))
    for dj in [j, j + 1]:
        tmp = abs(D - (a + dj * dj))
        res = min(res, tmp)
print(res)
