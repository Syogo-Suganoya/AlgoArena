# H: 行数, W: 列数
H, W = map(int, input().split())
# ボードを文字列リストとして取得
A = [input().strip() for _ in range(H)]

# dp[y][x] := (y,x) から右下まで最適に進んだときのスコア差
# 正ならTakahashiが有利、負ならAokiが有利
dp = [[0] * W for _ in range(H)]

# 右下から左上に向かって計算する（ボトムアップ）
for y in reversed(range(H)):
    for x in reversed(range(W)):
        # ゴール地点はスコア差0
        if x == W - 1 and y == H - 1:
            dp[y][x] = 0
            continue

        # ターンの判定: (x+y) が偶数ならTakahashi, 奇数ならAoki
        turn = (x + y) % 2  # 0: Takahashi, 1: Aoki

        candidates = []

        # 下方向に進む場合
        if y + 1 < H:
            # 次のマスの記号に応じてスコア差を計算
            val = 1 if A[y + 1][x] == "+" else -1
            # 先手なら加算、後手なら減算
            candidates.append(dp[y + 1][x] + (val if turn == 0 else -val))

        # 右方向に進む場合
        if x + 1 < W:
            val = 1 if A[y][x + 1] == "+" else -1
            candidates.append(dp[y][x + 1] + (val if turn == 0 else -val))

        # Takahashiはスコアを最大化、Aokiは最小化
        dp[y][x] = max(candidates) if turn == 0 else min(candidates)

# スタート地点の最終スコア差を取得
opt = dp[0][0]

# 結果判定
if opt > 0:
    print("Takahashi")
elif opt < 0:
    print("Aoki")
else:
    print("Draw")
