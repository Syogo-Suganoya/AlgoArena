N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
S = input()

from collections import defaultdict

# y座標ごとに、RとLのx座標を分けて保存
R = defaultdict(list)
L = defaultdict(list)

for i in range(N):
    x, y = XY[i]
    if S[i] == "R":
        R[y].append(x)
    else:
        L[y].append(x)

# 各yごとに、Rの人が左、Lの人が右にいれば衝突の可能性がある
for y in R:
    if y in L:
        maxR = min(R[y])  # R側の最も左（小さいx）
        minL = max(L[y])  # L側の最も右（大きいx）

        if maxR < minL:
            print("Yes")
            exit()

print("No")
