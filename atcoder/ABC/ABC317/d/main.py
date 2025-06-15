import sys

INF = 10**18

N = int(sys.stdin.readline())
X, Y, Z = [], [], []
S = 0
for _ in range(N):
    xi, yi, zi = map(int, sys.stdin.readline().split())
    X.append(xi)
    Y.append(yi)
    Z.append(zi)
    S += zi

# 過半数の議席ライン
half = (S + 1) // 2

# 選挙区ごとのコスト Wi を計算
costs = [max(0, (yi - xi + 1) // 2) for xi, yi in zip(X, Y)]

# DP 初期化
dp = [INF] * (S + 1)
dp[0] = 0

# ナップサック遷移
for wi, zi in zip(costs, Z):
    for j in range(S, zi - 1, -1):
        dp[j] = min(dp[j], dp[j - zi] + wi)

# 過半数以上の最小コストを取得
answer = min(dp[half:])
print(answer)
