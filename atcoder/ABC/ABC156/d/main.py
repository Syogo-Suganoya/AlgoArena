MOD = 10**9 + 7


# nCk を高速に求めるための関数（フェルマーの小定理使用）
def comb(n, k):
    if k < 0 or k > n:
        return 0

    # 分子 n*(n-1)*...*(n-k+1)
    numer = 1
    for i in range(k):
        numer = numer * (n - i) % MOD

    # 分母 k! を mod 逆元で割る
    denom = 1
    for i in range(1, k + 1):
        denom = denom * i % MOD

    # 逆元（a^(MOD-2) mod MOD）
    return numer * pow(denom, MOD - 2, MOD) % MOD


n, a, b = map(int, input().split())

total = pow(2, n, MOD) - 1  # 2^n - 1（空集合を引く）
bad_a = comb(n, a)  # 大きさ a の集合
bad_b = comb(n, b)  # 大きさ b の集合

ans = (total - bad_a - bad_b) % MOD
print(ans)
