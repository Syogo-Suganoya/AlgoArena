N = int(input())
A = list(map(int, input().split()))  # 長さ N-1
B = list(map(int, input().split()))  # 長さ N-1

# dp[i]: マス i に到達できる時の最大スコア（未到達は -inf）
INF = -(10**18)
dp = [INF] * (N + 1)
dp[1] = 0  # スタート地点

for i in range(1, N):
    if dp[i] == INF:
        continue  # 到達不可ならスキップ

    # A を選んで進む場合
    nxt = A[i - 1]
    dp[nxt] = max(dp[nxt], dp[i] + 100)

    # B を選んで進む場合
    nxt = B[i - 1]
    dp[nxt] = max(dp[nxt], dp[i] + 150)

print(dp[N])
