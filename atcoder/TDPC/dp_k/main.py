from bisect import bisect_left

N = int(input())
A = []
for _ in range(N):
    x, r = map(int, input().split())
    l = x - r  # 区間の左端（円の左端）
    r = x + r  # 区間の右端（円の右端）
    A.append((l, r))

# 区間をソート
# -l: 左端が大きい順に並べたい（内側の円は左端が右に寄っているため）
# -r: 左端が同じなら右端が大きいものを優先（包含関係を崩さないため）
A.sort(key=lambda a: (-a[0], -a[1]))

L = []  # LIS を求めるための配列（右端の候補を管理）

for l, r in A:
    # r を挿入できる位置を探す（二分探索）
    idx = bisect_left(L, r)
    if idx == len(L):
        # LIS の末尾に追加できる場合 → 新しい長さができる
        L.append(r)
    else:
        # 既存の位置に置き換え → 将来のためにより小さい値で更新
        L[idx] = r

# LIS の長さ = 包含できる円の最大個数
print(len(L))
