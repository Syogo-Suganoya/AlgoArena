MOD = 10**9 + 7


# ---------------------------------------
# nCr を高速に求めるための前計算
# ---------------------------------------
def prepare_comb(max_n):
    fact = [1] * (max_n + 1)
    inv = [1] * (max_n + 1)
    fact_inv = [1] * (max_n + 1)

    # 階乗を作る
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD

    # fact[max_n] の逆元を計算（フェルマーの小定理）
    fact_inv[max_n] = pow(fact[max_n], MOD - 2, MOD)

    # 階乗逆元を逆順に作っていく
    for i in range(max_n, 0, -1):
        fact_inv[i - 1] = fact_inv[i] * i % MOD

    # n の逆元
    for i in range(1, max_n + 1):
        inv[i] = fact[i - 1] * fact_inv[i] % MOD

    return fact, fact_inv


# nCr
def comb(n, r, fact, fact_inv):
    if r < 0 or r > n:
        return 0
    return fact[n] * fact_inv[r] % MOD * fact_inv[n - r] % MOD


# ---------------------------------------
# ここから問題処理
# ---------------------------------------
N, K = map(int, input().split())

# 重複組合せ H(a, b) = C(a+b-1, b) を使うため
# 最大で使う n は N + N 程度
MAX = 2 * N + 5
fact, fact_inv = prepare_comb(MAX)

# z は「空き部屋の数」
# 空き部屋 z は最大 min(N-1, K)
limit = min(N - 1, K)

ans = 0

for z in range(limit + 1):
    # 1) N 個の部屋から z 個を空きにする
    ways_choose_empty = comb(N, z, fact, fact_inv)

    # 2) 残り N - z 部屋に N 人を配る（各部屋 1 人以上）
    #    → 重複組合せ H(N - z, z)
    #       H(a, b) = C(a + b - 1, b)
    ways_assign_people = comb((N - z) + z - 1, z, fact, fact_inv)

    ans = (ans + ways_choose_empty * ways_assign_people) % MOD

print(ans)
