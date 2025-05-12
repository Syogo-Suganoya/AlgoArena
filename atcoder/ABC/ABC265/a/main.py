X, Y, N = map(int, input().split())

res = 100 * Y
for i in range(N + 1):
    rest = N - i
    if rest % 3 != 0:
        continue
    tmp = i * X + rest / 3 * Y
    res = min(res, tmp)
print(int(res))
