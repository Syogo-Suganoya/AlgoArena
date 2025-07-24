N = int(input())

Mod = 998244353
r = len(str(N))

TEN = [1] * (r + 1)
for d in range(1, r + 1):
    TEN[d] = (10 * TEN[d - 1]) % Mod

two_inv = pow(2, Mod - 2, Mod)

X = 0
for d in range(1, r):
    X += TEN[d - 1] * (9 * TEN[d - 1] + 1)
    X %= Mod

alpha = 9 * two_inv % Mod
X = (alpha * X) % Mod

N_mod = N % Mod
Y = (N_mod - TEN[r - 1] + 1) * (N_mod - TEN[r - 1] + 2) % Mod
Y = (two_inv * Y) % Mod

print((X + Y) % Mod)
