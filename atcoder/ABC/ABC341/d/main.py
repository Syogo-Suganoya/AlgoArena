import math

N, M, K = map(int, input().split())
L = N // math.gcd(N, M) * M  # 最小公倍数


def count_ok(x):
    return x // N + x // M - 2 * (x // L)


low, high = 0, 10**20  # 十分大きな上限
while high - low > 1:
    mid = (low + high) // 2
    if count_ok(mid) >= K:
        high = mid
    else:
        low = mid

print(high)
