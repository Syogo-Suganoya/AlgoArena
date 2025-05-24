N = int(input())

dp = [0] * (N + 2)  # N+2 にしておくと、N=1 のときも安心
dp[0] = 1  # 0 段目に到達する方法は 1 通り（何もしない）
dp[1] = 1  # 1 段目に到達する方法は 1 通り（1 段上る）

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
