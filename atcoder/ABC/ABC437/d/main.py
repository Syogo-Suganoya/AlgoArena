import bisect

MOD = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

cumB = [0] * (M + 1)
for i in range(M):
    cumB[i + 1] = (cumB[i] + B[i]) % MOD

res = 0

for a in A:
    idx = bisect.bisect_right(B, a)
    sum_pos = (a * idx - cumB[idx]) % MOD
    sum_neg = (cumB[M] - cumB[idx] - a * (M - idx)) % MOD
    res = (res + sum_pos + sum_neg) % MOD

print(res)
