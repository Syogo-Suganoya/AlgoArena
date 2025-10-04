INF = -(10**9)
N, M, K = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# cnt[l][r] を 1-index で使う（l ≤ r）
cnt = [[0] * (N + 1) for _ in range(N + 1)]
# 各繋がり (a, b) について、すべての l ≤ a ≤ b ≤ r の区間に +1
for a, b in edges:
    # a < b 保証されてる
    for l in range(1, a + 1):
        for r in range(b, N + 1):
            cnt[l][r] += 1

# dp[i][k] = ページ 1..i を k 章に分けたときの最大良さ
dp = [[INF] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for k in range(1, K + 1):
        # j は前の区切り点
        for j in range(0, i):
            if dp[j][k - 1] == INF:
                continue
            dp[i][k] = max(dp[i][k], dp[j][k - 1] + cnt[j + 1][i])

# 答え：N ページを K 章で分けたときの最大良さ
ans = dp[N][K]
print(ans)
