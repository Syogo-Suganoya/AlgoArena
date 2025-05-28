import math
from collections import defaultdict


def factorization(n):
    """
    数 n の平方因子（指数が奇数の素因数の積）を求める関数。
    例えば n=12=2^2*3^1 の場合、3^1の部分だけ残るので返り値は3。
    """
    res = 1
    for i in range(2, int(math.isqrt(n)) + 1):
        count = 0
        # 素因数 i で割れるだけ割る
        while n % i == 0:
            n //= i
            count += 1
        # 指数が奇数なら、その素因数を掛ける
        if count % 2 == 1:
            res *= i
    # 残りの素数があれば、指数1なので掛ける
    if n > 1:
        res *= n
    return res


N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)  # 平方因子ごとの出現回数
zero_count = 0  # 0 の数をカウント

for a in A:
    if a == 0:
        # 0 は特別扱い：積が常に平方数
        zero_count += 1
    else:
        # 0 以外なら平方因子を求めてカウント
        key = factorization(a)
        count[key] += 1

# 0 を含むペアの数を計算
# 0と他の非0要素のペアの数 + 0同士のペアの数
ans = zero_count * (N - zero_count) + zero_count * (zero_count - 1) // 2

# 同じ平方因子を持つ数同士のペアの数を計算
# 同じ平方因子を持つ要素のペアは積が平方数になる
for v in count.values():
    ans += v * (v - 1) // 2

print(ans)
