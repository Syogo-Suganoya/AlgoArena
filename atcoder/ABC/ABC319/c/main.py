import math
from itertools import permutations

# 3x3 の盤面を1次元のリストに変換
C = [list(map(int, input().split())) for _ in range(3)]
flat = [C[i][j] for i in range(3) for j in range(3)]

# 判定対象のライン（行・列・斜め）

lines = []
lines += [(0, 1, 2), (3, 4, 5), (6, 7, 8)]  # 行
lines += [(0, 3, 6), (1, 4, 7), (2, 5, 8)]  # 列
lines += [(0, 4, 8), (2, 4, 6)]  # 斜め

total = math.factorial(9)
good = 0

# すべての順列を調べる
for perm in permutations(range(9)):
    ok = True
    for a, b, c in lines:
        # 各セルの開けられる順番と中身を記録して、順番順に並べ替える
        open_order = sorted([
            (perm[a], flat[a]),
            (perm[b], flat[b]),
            (perm[c], flat[c]),
        ])
        # 最初の2つが同じ数字で、3つ目が違う → がっかり
        if (
            open_order[0][1] == open_order[1][1]
            and open_order[2][1] != open_order[0][1]
        ):
            ok = False
            break
    if ok:
        good += 1

# 確率を出力（浮動小数点）
print(good / total)
