N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和
P = [0] * (N + 1)
for i in range(N):
    P[i + 1] = P[i] + A[i]

# 区間和の最大を求める
max_sum = 0
for i in range(N - K + 1):
    s = P[i + K] - P[i]
    max_sum = max(max_sum, s)

# 期待値の最大は一度だけ計算
ans = (max_sum + K) / 2
print(ans)
