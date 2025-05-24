MOD = 10**9 + 7
N = int(input())

a, b = 1, 1
for _ in range(N - 2):
    a, b = b, (a + b) % MOD

print(b if N > 1 else 1)
