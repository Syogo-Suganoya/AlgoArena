import math

from sympy.ntheory import factorint


def prime_factors_count(N):
    """Nの素因数の個数をsympyを使って数える"""
    # factorint(N) は {素因数: 指数} の辞書を返す
    factorization = factorint(N)
    # 素因数の総個数を計算（指数の合計）
    return sum(factorization.values())


def min_magic_count(N):
    """Nを素因数分解し、必要な魔法の回数を求める"""
    # 素因数の個数を計算
    k = prime_factors_count(N)
    # 必要な魔法の回数を計算
    return math.ceil(math.log2(k))


# 入力と実行
N = int(input())
print(min_magic_count(N))
