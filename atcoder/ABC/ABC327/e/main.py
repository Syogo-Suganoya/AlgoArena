import math

N = int(input())
P = list(map(int, input().split()))

# dp[i][j] := i 回目までのコンテストから j 回選んだときの
# "重み付きパフォーマンスの合計" の最大値
# ここで重みは 0.9^(j-i) の形で次第に小さくなる
dp = [[0] * (N + 1) for _ in range(N + 1)]

# 動的計画法で dp を埋める
for i in range(N):
    for j in range(i + 1):
        # i 回目のコンテストを選ぶ場合と選ばない場合で最大を取る
        # 選ぶ場合は前の値に 0.9 を掛けて、今回の P[i] を加える
        # 選ばない場合は前の値をそのまま引き継ぐ
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j] * 0.9 + P[i])

# 最終的なレートの最大値を求める
result = float("-inf")  # 初期値は十分小さくしておく

# 各選択数 i (1回以上のコンテストを選ぶ) に対して計算
for i in range(1, N + 1):
    # 分母の計算：選んだコンテストの重みの合計
    denominator = sum(0.9 ** (i - j - 1) for j in range(i))

    # レート計算式
    # dp[N][i] / denominator → 重み付き平均パフォーマンス
    # 1200 / sqrt(i) → 選んだ回数に応じたペナルティ
    rate = dp[N][i] / denominator - 1200.0 / math.sqrt(i)

    # 最大値を更新
    result = max(result, rate)

# 答えを出力
print(result)
