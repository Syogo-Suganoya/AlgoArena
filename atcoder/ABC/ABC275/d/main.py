import sys

sys.setrecursionlimit(10**6)

from functools import lru_cache

N = int(input())


@lru_cache(maxsize=None)
def f(k):
    if k == 0:
        return 1
    return f(k // 2) + f(k // 3)


print(f(N))
