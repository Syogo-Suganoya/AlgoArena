N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

# x: 行ブロック番号、y: 列内の位置
x = [[0] * M for _ in range(N)]
y = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        x[i][j] = (B[i][j] + 6) // 7  # 上方向ブロック番号
        y[i][j] = (B[i][j] - 1) % 7 + 1  # 横方向で1~7の位置

ans = "Yes"

for i in range(N):
    for j in range(M):
        # 縦方向のブロックが連続しているか
        if i > 0 and x[i][j] != x[i - 1][j] + 1:
            ans = "No"
        # 横方向の値が連続しているか
        if j > 0 and y[i][j] != y[i][j - 1] + 1:
            ans = "No"
        # 縦方向で横ブロックが揃っているか
        if j > 0 and x[i][j] != x[i][j - 1]:
            ans = "No"
        # 横方向で縦ブロックが揃っているか
        if i > 0 and y[i][j] != y[i - 1][j]:
            ans = "No"

print(ans)
