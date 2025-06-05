H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# DPテーブルの初期化（各マスに到達できる最大の経路長を保持）
dp = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            continue  # 壁のマスは通れないのでスキップ

        if i == 0 and j == 0:
            dp[i][j] = 1  # スタート地点
        else:
            # 上から来られる場合
            if i > 0 and dp[i - 1][j] > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)

            # 左から来られる場合
            if j > 0 and dp[i][j - 1] > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)

# 最も長く移動できた経路の長さを出力
ans = 0
for row in dp:
    ans = max(ans, max(row))
print(ans)
