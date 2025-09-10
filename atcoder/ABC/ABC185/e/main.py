n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**9
dp = [[INF] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n + 1):
    for j in range(m + 1):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)  # A を削る
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)  # B を削る
        if i > 0 and j > 0:
            cost = 0 if A[i - 1] == B[j - 1] else 1
            dp[i][j] = min(
                dp[i][j], dp[i - 1][j - 1] + cost
            )  # 比較してペナルティ加える

print(dp[n][m])
