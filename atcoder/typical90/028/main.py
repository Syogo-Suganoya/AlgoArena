# 二次元いもす法
def imos_2d(H, W, queries):
    # Step 1: 差分配列の作成
    grid = [[0] * (W + 1) for _ in range(H + 1)]

    value = 1

    # 各クエリを差分配列に反映
    for x1, y1, x2, y2 in queries:
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


N = int(input())
t = []
for _ in range(N):
    S = list(map(int, input().split()))
    t.append(S)

H = W = 1001
res = imos_2d(H, W, t)

ans = [0] * (N + 1)
for i in range(len(res)):
    for j in range(len(res[i])):
        num = res[i][j]
        if num == 0:
            continue
        ans[num] += 1

for i in range(1, N + 1):
    print(ans[i])
