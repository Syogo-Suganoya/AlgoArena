MOD = 998244353  # 問題の指定 MOD

# 入力: N 人、M 色
N, M = map(int, input().split())

# 階乗と逆元の前計算
fact = [1] * (N + 1)  # fact[i] = i! % MOD
invfact = [1] * (N + 1)  # invfact[i] = (i!)^-1 % MOD
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % MOD

# n! の逆元を MOD で計算（フェルマーの小定理）
invfact[N] = pow(fact[N], MOD - 2, MOD)
for i in range(N - 1, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


# 組み合わせ計算 nCr
def choose(n, r):
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


ans = 0
for k in range(N + 1):
    # 包除原理の符号 (-1)^k
    sign = -1 if k % 2 else 1

    # N-k 人を自由に色塗りする場合の数
    # max(1, N-k) は全員除外したときに 0 乗を避けるため
    ways = pow(M, max(1, N - k), MOD)

    # k 人を選ぶ方法の数
    comb = choose(N, k)

    # 足し引きして合計
    ans += sign * ways * comb % MOD
    ans %= MOD  # MOD でまとめておく

print(ans % MOD)
