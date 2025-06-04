def f(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


N = int(input())
ans = 10**20  # 十分大きな初期値

for a in range(10**6 + 1):
    left = -1
    right = 10**6 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if f(a, mid) >= N:
            right = mid
        else:
            left = mid
    ans = min(ans, f(a, right))

print(ans)
