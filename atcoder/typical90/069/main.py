MOD = 1000000007


def binpower(a, b):
    ans = 1
    while b != 0:
        if b % 2 == 1:
            ans = (ans * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return ans


N, K = map(int, input().split())
if K == 1:
    print(1 if N == 1 else 0)
elif N == 1:
    print(K % MOD)
elif N == 2:
    print((K * (K - 1)) % MOD)
else:
    print((K * (K - 1) % MOD) * binpower(K - 2, N - 2) % MOD)
