MOD = 10**9 + 7

# 階乗と逆元の前計算をしておく
MAX = 10**6 + 5
fac = [1] * MAX
inv = [1] * MAX
for i in range(1, MAX):
    fac[i] = fac[i - 1] * i % MOD
inv[MAX - 1] = pow(fac[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, -1, -1):
    inv[i] = inv[i + 1] * (i + 1) % MOD


def comb(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return fac[n] * inv[k] % MOD * inv[n - k] % MOD


X, Y = map(int, input().split())

# 到達可能性の確認
if (X + Y) % 3 != 0:
    print(0)
    exit()

m = (X + Y) // 3
a = m * 2 - Y  # 移動パターン (2,1) の回数
b = m * 2 - X  # 移動パターン (1,2) の回数

if a < 0 or b < 0 or a + b != m:
    print(0)
else:
    print(comb(a + b, a))
