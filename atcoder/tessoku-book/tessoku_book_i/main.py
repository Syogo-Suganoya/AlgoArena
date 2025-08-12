H, W, N = map(int, input().split())
grid = [[0] * (W + 2) for _ in range(H + 2)]  # 境界外アクセス防止のため +2

for _ in range(N):
    A, B, C, D = map(int, input().split())
    grid[A][B] += 1
    grid[C + 1][B] -= 1
    grid[A][D + 1] -= 1
    grid[C + 1][D + 1] += 1

# 縦方向累積和
for y in range(1, H + 1):
    for x in range(1, W + 1):
        grid[y][x] += grid[y - 1][x]

# 横方向累積和
for y in range(1, H + 1):
    for x in range(1, W + 1):
        grid[y][x] += grid[y][x - 1]

# 出力（1-based 部分だけ）
for y in range(1, H + 1):
    print(*grid[y][1 : W + 1])
