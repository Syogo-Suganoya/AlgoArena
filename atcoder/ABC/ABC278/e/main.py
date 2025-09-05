from collections import defaultdict

# 入力
H, W, N, h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

# 数字ごとの座標をまとめる
positions = defaultdict(list)
for i in range(H):
    for j in range(W):
        positions[grid[i][j]].append((i + 1, j + 1))  # 1-indexにして計算を簡単に

# imos法用の2次元配列を作成
imos = [[0] * (W - w + 2) for _ in range(H - h + 2)]

# 数字ごとに、部分グリッドに含まれない範囲を加算
for key, coords in positions.items():
    ks, ls = 0, 0
    kt, lt = H - h + 1, W - w + 1
    for i, j in coords:
        ks = max(ks, i - h)
        ls = max(ls, j - w)
        kt = min(kt, i)
        lt = min(lt, j)
    if ks < kt and ls < lt:
        imos[ks][ls] += 1
        imos[ks][lt] -= 1
        imos[kt][ls] -= 1
        imos[kt][lt] += 1

# 列方向の累積和
for i in range(H - h + 1):
    for j in range(W - w + 1):
        imos[i][j + 1] += imos[i][j]

# 行方向の累積和
for i in range(H - h + 1):
    for j in range(W - w + 1):
        imos[i + 1][j] += imos[i][j]

# 答えの計算と出力
for i in range(H - h + 1):
    ans_row = [len(positions) - imos[i][j] for j in range(W - w + 1)]
    print(*ans_row)
