N = int(input())
MAX = 1501  # 座標上限 + 余裕分
imos = [[0] * (MAX + 1) for _ in range(MAX + 1)]

# 2D 差分更新（Imos 法）
for _ in range(N):
    A, B, C, D = map(int, input().split())
    imos[A][B] += 1
    imos[C][B] -= 1
    imos[A][D] -= 1
    imos[C][D] += 1

# 横方向の累積和
for x in range(MAX):
    for y in range(1, MAX):
        imos[x][y] += imos[x][y - 1]

# 縦方向の累積和
for x in range(1, MAX):
    for y in range(MAX):
        imos[x][y] += imos[x - 1][y]

# 少なくとも1枚に覆われているマスの面積をカウント
ans = 0
for x in range(MAX):
    for y in range(MAX):
        if imos[x][y] > 0:
            ans += 1

print(ans)
