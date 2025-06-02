from math import prod

MOD = 998244353
A = list(map(int, input().split()))

result = prod(A[:3]) % MOD - prod(A[3:]) % MOD
print(result % MOD)
