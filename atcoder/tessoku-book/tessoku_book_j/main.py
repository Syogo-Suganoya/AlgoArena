N = int(input())
A = list(map(int, input().split()))

# 左側の累積最大値
prefix = [0] * N
prefix[0] = A[0]
for i in range(1, N):
    prefix[i] = max(prefix[i - 1], A[i])

# 右側の累積最大値
suffix = [0] * N
suffix[-1] = A[-1]
for i in range(N - 2, -1, -1):
    suffix[i] = max(suffix[i + 1], A[i])

D = int(input())
for _ in range(D):
    L, R = map(int, input().split())
    # L, R は1-indexedなので調整
    left_max = prefix[L - 2] if L > 1 else 0
    right_max = suffix[R] if R < N else 0
    print(max(left_max, right_max))
