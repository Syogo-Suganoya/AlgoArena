N = int(input())
queries = []
for _ in range(N):
    queries.append(list(map(int, input().split())))

H_MAX = 2005
W_MAX = 2005

grid = [[0] * W_MAX for _ in range(H_MAX)]

for u, d, l, r in queries:
    # 2次元いもす法
    grid[u][l] += 1
    grid[u][r + 1] -= 1
    grid[d + 1][l] -= 1
    grid[d + 1][r + 1] += 1

# 累積和
for i in range(H_MAX):
    for j in range(1, W_MAX):
        grid[i][j] += grid[i][j - 1]
for j in range(W_MAX):
    for i in range(1, H_MAX):
        grid[i][j] += grid[i - 1][j]

# 1以上
more_one_cnt = 0
# ちょうど1
ones_grid = [[0] * W_MAX for _ in range(H_MAX)]
for i in range(1, H_MAX):
    for j in range(1, W_MAX):
        val = grid[i][j]
        if val > 0:
            more_one_cnt += 1
        if val == 1:
            ones_grid[i][j] = 1

# ちょうど1の累積和
ones_acc = [[0] * W_MAX for _ in range(H_MAX)]
for i in range(1, H_MAX):
    for j in range(1, W_MAX):
        ones_acc[i][j] = (
            ones_acc[i - 1][j]
            + ones_acc[i][j - 1]
            - ones_acc[i - 1][j - 1]
            + ones_grid[i][j]
        )

# 全体マス数
TOTAL_CELLS = 4000000

for u, d, l, r in queries:
    # その区間
    cnt = (
        ones_acc[d][r]
        - ones_acc[u - 1][r]
        - ones_acc[d][l - 1]
        + ones_acc[u - 1][l - 1]
    )
    # 消えたあと
    remain = more_one_cnt - cnt
    print(TOTAL_CELLS - remain)
