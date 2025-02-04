N = int(input())
A = list(map(int, input().split()))

MOD = 10**8

A.sort()
r = N
cnt = 0
res = 0

for i in range(N):
    r = max(r, i + 1)
    while r - 1 > i and A[r - 1] + A[i] >= MOD:
        r -= 1
    cnt += N - r

for i in range(N):
    res += A[i] * (N - 1)

res -= cnt * MOD
print(res)
