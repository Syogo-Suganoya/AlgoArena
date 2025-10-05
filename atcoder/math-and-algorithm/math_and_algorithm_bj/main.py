def sum_abs_diff(arr):
    arr.sort()
    res = 0
    s = 0  # 累積和
    for i, v in enumerate(arr):
        # 各 v が前のすべての点との差を足す
        res += v * i - s
        s += v
    return res


N = int(input().strip())
xs = []
ys = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
ans = sum_abs_diff(xs) + sum_abs_diff(ys)
print(ans)
