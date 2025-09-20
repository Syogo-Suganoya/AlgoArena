from collections import Counter


def prime_factorize(n: int):
    """nを素因数分解して {素数: 指数} を返す"""
    factors = Counter()
    x = n
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors[d] += 1
            x //= d
        d += 1
    if x > 1:
        factors[x] += 1
    return factors


N = int(input())

# 1. N! の素因数分解を作る
total = Counter()
for i in range(2, N + 1):
    total += prime_factorize(i)

# 2. 各素数の指数をリスト化
exps = list(total.values())

# 3. パターンに当てはめて数える
ans = 0

# (A) 75 = 75 → 指数 >= 74 が1つ
ans += sum(1 for e in exps if e >= 74)

# (B) 75 = 25 * 3 → 指数 >= 24 が1つ & 指数 >= 2 が別に1つ
for i in range(len(exps)):
    if exps[i] >= 24:
        for j in range(len(exps)):
            if i != j and exps[j] >= 2:
                ans += 1

# (C) 75 = 15 * 5 → 指数 >= 14 が1つ & 指数 >= 4 が別に1つ
for i in range(len(exps)):
    if exps[i] >= 14:
        for j in range(len(exps)):
            if i != j and exps[j] >= 4:
                ans += 1

# (D) 75 = 5 * 5 * 3 → 指数 >= 4 が2つ & 指数 >= 2 が1つ
for i in range(len(exps)):
    if exps[i] >= 4:
        for j in range(i + 1, len(exps)):
            if exps[j] >= 4:
                for k in range(len(exps)):
                    if k != i and k != j and exps[k] >= 2:
                        ans += 1

print(ans)
