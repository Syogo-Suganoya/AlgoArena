import bisect

MOD = 1_000_000_007

N, W, L, R = map(int, input().split())
A = list(map(int, input().split()))
X = [0] + A + [W]

dp = [0] * (N + 2)
dp[0] = 1
cum = [0] * (N + 2)
cum[0] = 1

for i in range(1, N + 2):
    # X[j] がジャンプ可能な範囲のインデックス
    left_idx = bisect.bisect_left(X, X[i] - R)
    right_idx = bisect.bisect_right(X, X[i] - L) - 1
    if left_idx <= right_idx:
        dp[i] = (cum[right_idx] - (cum[left_idx - 1] if left_idx > 0 else 0)) % MOD
    cum[i] = (cum[i - 1] + dp[i]) % MOD

print(dp[N + 1])
