N = int(input())
R = []
C = []
for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

minR, maxR = min(R), max(R)
minC, maxC = min(C), max(C)

delta = max(maxR - minR, maxC - minC)
# 切り上げ (整数計算)
ans = (delta + 1) // 2
print(ans)
