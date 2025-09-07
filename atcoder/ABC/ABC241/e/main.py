N, K = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]: 2^i 回繰り返したときの、j からのアメの増加量
# と j' = (j + dp[i][j]) % N の組を保持する
LOG = K.bit_length()
dp_sum = [[0] * N for _ in range(LOG)]
dp_next = [[0] * N for _ in range(LOG)]

# 初期状態（2^0 = 1 回）
for j in range(N):
    dp_sum[0][j] = A[j]
    dp_next[0][j] = (j + A[j]) % N

# Doubling 構築
for i in range(LOG - 1):
    for j in range(N):
        mid = dp_next[i][j]
        dp_sum[i + 1][j] = dp_sum[i][j] + dp_sum[i][mid]
        dp_next[i + 1][j] = dp_next[i][mid]

# 実際の処理
res = 0
pos = 0
for i in range(LOG):
    if K >> i & 1:
        res += dp_sum[i][pos]
        pos = dp_next[i][pos]

print(res)
