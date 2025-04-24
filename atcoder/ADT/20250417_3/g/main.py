N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    Xi, Yi = map(int, input().split())
    x[i] = Xi
    y[i] = Yi

dp = [[-4 * 10**18 for _ in range(2)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    if x[i] == 0:
        dp[i + 1][0] = max(dp[i][0], max(dp[i][0], dp[i][1]) + y[i])
        dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])
    else:
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + y[i])
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])

print(max(dp[N][0], dp[N][1]))
