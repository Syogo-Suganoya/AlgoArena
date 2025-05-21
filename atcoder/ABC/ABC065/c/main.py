import math

MOD = 10**9 + 7

N, M = map(int, input().split())

if abs(N - M) > 1:
    print(0)
elif N == M:
    # 同じなら 2 × N! × M!
    print((math.factorial(N) * math.factorial(M) * 2) % MOD)
else:
    # 差が1なら N! × M!
    print((math.factorial(N) * math.factorial(M)) % MOD)
