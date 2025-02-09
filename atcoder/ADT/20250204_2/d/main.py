A, B, C, D, E, F = map(int, input().split())
MOD = 998244353

l = A * B * C
r = D * E * F

print((l - r) % MOD)
