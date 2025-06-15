import bisect

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(map(int, input().split()))

# 累積和（B_sum[i] は B[0]〜B[i-1] の合計）
B_sum = [0] * (M + 1)
for i in range(M):
    B_sum[i + 1] = B_sum[i] + B[i]

res = 0
for a in A:
    rem = P - a
    idx = bisect.bisect_right(B, rem)
    # B[0]〜B[idx-1] までは P を超えない
    res += a * idx + B_sum[idx]
    res += (M - idx) * P

print(res)
