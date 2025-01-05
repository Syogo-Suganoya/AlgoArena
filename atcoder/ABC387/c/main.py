# 公式解説から引用
# https://atcoder.jp/contests/abc387/submissions/61401454

l, r = map(int, input().split())
dp = {}


def f(n, k):
    if n <= 0:
        return 0
    if (n, k) in dp:
        return dp[n, k]
    res = 0
    for i in range(10):
        res += f((n - i) // 10, max(k, i))
    res += max(min(n, 9) - k, 0)
    dp[n, k] = res
    return res


ans = f(r, 0) - f(l - 1, 0)
print(ans)
