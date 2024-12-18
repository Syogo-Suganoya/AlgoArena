N, L = map(int, input().split())

dp = [0] * (N + 1)
mod = 10**9 + 7

dp[0] = 1
for i in range(1, N + 1):
    dp[i] = dp[i - 1]
    skip = i - L
    if 0 <= skip <= N:
        dp[i] = (dp[i - 1] + dp[skip]) % mod

print(dp[-1])
