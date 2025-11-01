# 金・銀・銅の初期枚数を入力
A, B, C = map(int, input().split())

# 最大枚数を100として3次元DPを用意
# dp[i][j][k] := 金i枚, 銀j枚, 銅k枚の状態から終了までにかかる期待操作回数
dp = [[[0.0] * 101 for _ in range(101)] for _ in range(101)]

# 逆順に計算していく（大きい枚数から小さい枚数へ）
for i in range(100, -1, -1):
    for j in range(100, -1, -1):
        for k in range(100, -1, -1):
            # いずれかが100枚に到達した状態は終了状態
            if i == 100 or j == 100 or k == 100:
                dp[i][j][k] = 0.0
                continue

            total = i + j + k  # 現在の総コイン枚数
            expected = 1.0  # 今回の操作1回をカウント

            # 金貨を選ぶ確率は i / total
            if i > 0:
                expected += (i / total) * dp[i + 1][j][k]
            # 銀貨を選ぶ確率は j / total
            if j > 0:
                expected += (j / total) * dp[i][j + 1][k]
            # 銅貨を選ぶ確率は k / total
            if k > 0:
                expected += (k / total) * dp[i][j][k + 1]

            # 期待値を総枚数で割って確率で平均化
            dp[i][j][k] = expected / ((i + j + k) / total if total > 0 else 1)

# 初期状態からの期待値を出力
print(dp[A][B][C])
