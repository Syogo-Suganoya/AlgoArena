N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

H = W = 100


def imos_2d(H, W, queries):
    # Step 1: 差分配列の作成
    grid = [[0] * (W + 1) for _ in range(H + 1)]

    # 各クエリを差分配列に反映
    for A, B, C, D in queries:
        x1, y1, x2, y2 = A, C, B, D
        value = 1
        grid[x1][y1] += value
        grid[x2][y2] += value
        grid[x1][y2] -= value
        grid[x2][y1] -= value

    # Step 2: 横方向の累積和
    for x in range(H + 1):
        for y in range(1, W + 1):
            grid[x][y] += grid[x][y - 1]

    # Step 3: 縦方向の累積和
    for y in range(W + 1):
        for x in range(1, H + 1):
            grid[x][y] += grid[x - 1][y]

    # グリッドのサイズを調整（余分な行列を削除）
    result = [row[:W] for row in grid[:H]]
    return result


r = imos_2d(H, W, A)

res = 0
for i in range(H):
    for j in range(W):
        if r[i][j] > 0:
            res += 1
print(res)
