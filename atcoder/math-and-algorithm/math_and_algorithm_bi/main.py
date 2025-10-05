MOD = 10**9 + 7


def modinv(x):
    return pow(x, MOD - 2, MOD)


def precompute_factorials(n):
    fact = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv[n] = modinv(fact[n])
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % MOD
    return fact, inv


def comb(n, k, fact, inv):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD


N = int(input().strip())
A = list(map(int, input().split()))

fact, inv = precompute_factorials(N - 1)

ans = 0
# i from 1 to N, but Python のインデックスは 0-based
for i in range(N):
    # 二項係数 C(N-1, i)
    c = comb(N - 1, i, fact, inv)
    ans = (ans + c * A[i]) % MOD

print(ans)
