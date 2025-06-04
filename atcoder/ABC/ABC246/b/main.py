import math

A, B = map(int, input().split())

# (0, 0) から (A, B) までのユークリッド距離
dist = math.hypot(A, B)

# 距離を1減らす（ただし0未満にならないように制限）
dist -= 1
if dist < 0:
    dist = 0

# ベクトル (A, B) の単位ベクトル
if A == 0 and B == 0:
    x = y = 0
else:
    unit_x = A / math.hypot(A, B)
    unit_y = B / math.hypot(A, B)

    # (A, B) から距離 dist だけ戻る（逆方向）
    x = A - unit_x * dist
    y = B - unit_y * dist

print(f"{x:.10f} {y:.10f}")
