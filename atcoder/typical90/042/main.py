MOD = 10**9 + 7


def count_numbers():
    if K % 9 != 0:
        return 0
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(1, K + 1):
        for d in range(1, 10):
            if i - d >= 0:
                dp[i] = (dp[i] + dp[i - d]) % MOD
    return dp[K]


K = int(input())

# 出力
print(count_numbers())
