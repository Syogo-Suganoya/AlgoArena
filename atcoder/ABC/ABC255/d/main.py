import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# 累積和の計算
S = [0]
for a in A:
    S.append(S[-1] + a)

for _ in range(Q):
    # 理想と実際の累積和の差を求める
    x = int(input())
    idx = bisect.bisect_left(A, x)
    # A[0]〜A[idx-1] は x 未満
    # A[idx]〜A[N-1] は x 以上
    left = x * idx - S[idx]
    right = (S[N] - S[idx]) - x * (N - idx)
    print(left + right)
