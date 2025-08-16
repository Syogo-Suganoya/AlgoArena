N, M = map(int, input().split())
A = set(int(input()) for _ in range(M))  # 壊れた段を集合に入れる

mod = 10**9 + 7
dp = [0] * (N + 1)
dp[0] = 1  # 0段目にいる方法は1通り

for i in range(N):
    if dp[i] == 0:
        continue
    # 1段進む
    if i + 1 <= N and (i + 1) not in A:
        dp[i + 1] = (dp[i + 1] + dp[i]) % mod
    # 2段進む
    if i + 2 <= N and (i + 2) not in A:
        dp[i + 2] = (dp[i + 2] + dp[i]) % mod

print(dp[N])
