import math


def simple_sieve(n):
    """1 ～ n までの素数を列挙する（普通のエラトステネス）"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, v in enumerate(is_prime) if v]
    return primes


def count_primes_in_interval(L, R):
    # ベース素数は sqrt(R) まで
    limit = int(math.isqrt(R)) + 1
    base_primes = simple_sieve(limit)

    seg_len = R - L + 1
    is_prime_seg = [True] * seg_len

    for p in base_primes:
        # 区間 [L, R] 内で p の倍数を見つける
        # 開始位置を決める
        start = (L + p - 1) // p * p  # L 以上の p の倍数
        if start < p * 2:
            start = p * 2
        for x in range(start, R + 1, p):
            is_prime_seg[x - L] = False

    if L == 1:
        is_prime_seg[0] = False

    # 真のものを数える
    count = 0
    for flag in is_prime_seg:
        if flag:
            count += 1
    return count


L, R = map(int, input().split())
ans = count_primes_in_interval(L, R)
print(ans)
