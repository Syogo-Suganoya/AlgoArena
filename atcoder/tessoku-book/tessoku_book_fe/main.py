import bisect

N = int(input())
A = list(map(int, input().split()))

A.sort()

# 累積和を作成
cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + A[i]

Q = int(input())
for _ in range(Q):
    X = int(input())
    idx = bisect.bisect_right(cum, X)
    print(idx - 1)
