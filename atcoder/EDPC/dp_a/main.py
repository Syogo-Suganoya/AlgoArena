# 入力読み込み
N = int(input())
h = list(map(int, input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

# 初期条件を入力
dp[0] = 0
dp[1] = abs(h[1] - h[0])

# 漸化式にしたがって DP を実装する
for i in range(2, N):
    # i を現在いる足場と考える。
    # i 番目の足場へ行く方法として i-i 番目からのジャンプと i-2 番目からのジャンプがある
    # 2 通りの行き方のうちコストの少ない方を dp[i] とする
    dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]), dp[i - 1] + abs(h[i] - h[i - 1]))

# dp 配列の末尾が N 番目の足場にたどり着くために必要なコストとなる
print(dp[-1])
