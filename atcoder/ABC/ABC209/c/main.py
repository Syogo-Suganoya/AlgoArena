MOD = 10**9 + 7  # 余りを取る modulus
N = int(input())
A = list(map(int, input().split()))

A.sort()
res = 1

for i, a in enumerate(A):
    res = res * (a - i) % MOD

print(res)
