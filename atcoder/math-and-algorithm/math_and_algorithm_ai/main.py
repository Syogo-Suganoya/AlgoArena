N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の初期化（0番目は0）
ar = [0] * (N + 1)
for i in range(N):
    ar[i + 1] = ar[i] + A[i]

# クエリ処理
for _ in range(Q):
    L, R = map(int, input().split())
    print(ar[R] - ar[L - 1])
