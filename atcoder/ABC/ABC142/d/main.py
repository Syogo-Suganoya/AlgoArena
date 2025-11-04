import math

from sympy import factorint

A, B = map(int, input().split())

# 最大公約数を求める
g = math.gcd(A, B)

# 素因数分解 (返り値は {素数: 指数} の辞書)
factors = factorint(g)

# 種類数 + 1 が答え
print(len(factors) + 1)
