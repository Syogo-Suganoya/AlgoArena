M = int(input())


def closest_power_of_three_exp(n):
    """
    n 以下の最大の3のべき乗の指数を求める。
    戻り値は (指数, nとの差)
    """
    exp = 0
    p = 1
    while p * 3 <= n:
        p *= 3
        exp += 1
    return exp, n - p


l = []

while M > 0:
    exp, M = closest_power_of_three_exp(M)
    l.append(exp)

print(len(l))
print(*l)
