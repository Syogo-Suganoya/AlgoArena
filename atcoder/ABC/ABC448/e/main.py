import sys

sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

MOD = 10007
M = MOD * Q


def repunit(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        half = repunit(n // 2)
        p = pow(10, n // 2, M)
        return (half * p + half) % M
    else:
        return (repunit(n - 1) * 10 + 1) % M


x = 0

for _ in range(N):
    c, l = map(int, input().split())

    p = pow(10, l, M)
    ones = repunit(l)

    add = (c * ones) % M
    x = (x * p + add) % M

ans = (x // Q) % MOD
print(ans)
