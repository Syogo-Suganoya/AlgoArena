n, m = map(int, input().split())
a = list(map(int, input().split()))

# 各操作 j で登場する値を記録するリスト
vals = [[] for _ in range(m + 1)]

for i in range(n):
    if a[i] >= n:
        continue

    # j の下限
    if a[i] >= 0:
        l = 1
    else:
        l = (-a[i] + i) // (i + 1)

    # j の上限
    r = min(m + 1, (n - a[i] + i) // (i + 1))

    # j = l, l+1, ..., r-1 のときに登場する値を登録
    for j in range(l, r):
        vals[j].append(a[i] + (i + 1) * j)

# 各 j について mex を計算
for j in range(1, m + 1):
    sz = len(vals[j])
    exi = [False] * (sz + 1)

    for v in vals[j]:
        if v < sz:
            exi[v] = True

    res = 0
    while exi[res]:
        res += 1

    print(res)
