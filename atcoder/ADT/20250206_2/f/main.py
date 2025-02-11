import bisect

N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)  # 数列Aの総和
k, m = divmod(X, sum_A)  # 何周分足せるか & 残りの和
cumsum = [0] * (N + 1)  # 累積和リスト

# 累積和を計算
for i in range(N):
    cumsum[i + 1] = cumsum[i] + A[i]

# `m` を超える最小の位置を `bisect_right` で探す
pos = bisect.bisect_right(cumsum, m)

# 結果を出力
print(k * N + pos)
