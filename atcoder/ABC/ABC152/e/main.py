import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

MOD = 10**9 + 7


def factorize(n):
    """
    n を素因数分解して {素数: 指数} の辞書を返す
    """
    res = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            res[d] += 1
            n //= d
        d += 1
    if n > 1:
        res[n] += 1
    return res


def modinv(a, m=MOD):
    """a の逆元を m を法として計算 (フェルマーの小定理)"""
    return pow(a, m - 2, m)


N = int(input())
A = list(map(int, input().split()))

# --- Step1: 各 A[i] を素因数分解し、LCM を構築するための最大指数を管理
lcm_factors = defaultdict(int)  # {素数: 最大指数}
fact_list = []
for a in A:
    f = factorize(a)
    fact_list.append(f)
    for p, e in f.items():
        lcm_factors[p] = max(lcm_factors[p], e)

# --- Step2: LCM を MOD で構築（素因数の最大指数を掛ける）
LCM = 1
for p, e in lcm_factors.items():
    LCM = (LCM * pow(p, e, MOD)) % MOD

# --- Step3: 各 B[i] = LCM / A[i] を計算して合計
ans = 0
for a in A:
    ans = (ans + LCM * modinv(a)) % MOD

print(ans)
