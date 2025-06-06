N = int(input())
A = list(map(int, input().split()))
A.sort()

# 累積和を準備（prefix_sum[i] = A[0] + A[1] + ... + A[i-1]）
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

res = 0
for i in range(N):
    # A[i] の前の累積和との差分を計算：
    #   res += A[i] * i - (A[0] + A[1] + ... + A[i-1])
    #       = A[i] * i - prefix_sum[i]
    res += A[i] * i - prefix_sum[i]

print(res)
