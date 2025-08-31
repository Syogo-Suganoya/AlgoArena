def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        memo[n] = n
        return n
    res = fib(n - 1, memo) + fib(n - 2, memo)
    res = str(res)[::-1]
    memo[n] = int(res)
    return memo[n]


N, M = map(int, input().split())

print(fib(10, {1: N, 2: M}))
