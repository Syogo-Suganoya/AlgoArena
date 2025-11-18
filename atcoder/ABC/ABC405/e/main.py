MOD = 998244353


# nCr 用に階乗と逆元を準備
def prepare_comb(n):
    fact = [1] * (n + 1)
    invfact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return fact, invfact


def comb(n, r, fact, invfact):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


# --- メイン ---
a, b, c, d = map(int, input().split())
N = a + b + c + d

# 最大で N まで使うので前計算
fact, invfact = prepare_comb(N)

ans = 0

# i = A の最後の位置（1-indexed）
# i は a〜(a+b) の範囲
for i in range(a, a + b + 1):
    left = comb(i - 1, a - 1, fact, invfact)  # 左側に A が a-1 個
    right = comb(N - i, c, fact, invfact)  # 右側に C が c 個
    ans = (ans + left * right) % MOD

print(ans)
