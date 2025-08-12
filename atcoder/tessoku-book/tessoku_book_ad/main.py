mod = 10**9 + 7

n, r = map(int, input().split())

# 階乗と逆元のテーブルを作る
fact = [1] * (n + 1)
inv_fact = [1] * (n + 1)

for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % mod

# フェルマーの小定理で逆元計算
inv_fact[n] = pow(fact[n], mod - 2, mod)
for i in reversed(range(n)):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod


def nCr(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod


print(nCr(n, r))
