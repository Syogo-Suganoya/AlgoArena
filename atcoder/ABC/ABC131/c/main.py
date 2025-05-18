import math

A, B, C, D = map(int, input().split())


def count_divisible(X, div):
    return X // div


# 各倍数の個数
c = count_divisible(B, C) - count_divisible(A - 1, C)
d = count_divisible(B, D) - count_divisible(A - 1, D)
cd = count_divisible(B, math.lcm(C, D)) - count_divisible(A - 1, math.lcm(C, D))

count = c + d - cd

# 全体から倍数を引く
print((B - A + 1) - count)
