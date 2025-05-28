import sys

sys.setrecursionlimit(10**7)

N = int(input())
memo = {}


def f(n):
    if n < 2:
        return 0
    if n in memo:
        return memo[n]
    a, b = n // 2, (n + 1) // 2
    res = n + f(a) + f(b)
    memo[n] = res
    return res


print(f(N))
