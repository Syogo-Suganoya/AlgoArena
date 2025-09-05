from collections import Counter

K = int(input())


# 素因数分解
def prime_factors(n):
    res = Counter()
    i = 2
    while i * i <= n:
        while n % i == 0:
            res[i] += 1
            n //= i
        i += 1
    if n > 1:
        res[n] += 1
    return res


pf = prime_factors(K)


# i! に含まれる素数 p の指数
def count_p_in_factorial(p, i):
    cnt = 0
    power = p
    while power <= i:
        cnt += i // power
        power *= p
    return cnt


ans = 0
for p, exp in pf.items():
    # 二分探索で p の指数が exp 以上になる最小 i を求める
    low, high = 1, K * 10  # 適当に大きめ
    while low < high:
        mid = (low + high) // 2
        if count_p_in_factorial(p, mid) >= exp:
            high = mid
        else:
            low = mid + 1
    ans = max(ans, low)

print(ans)
