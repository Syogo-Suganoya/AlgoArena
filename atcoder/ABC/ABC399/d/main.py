T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # 各カップルの出現位置を記録（0-indexed）
    pos = [[] for _ in range(N + 1)]
    for i, x in enumerate(A):
        pos[x].append(i)

    seen = set()
    ans = 0

    # 隣接ペア (A[i], A[i+1]) をすべて試す
    for i in range(2 * N - 1):
        a = A[i]
        b = A[i + 1]
        if a == b:
            continue

        pair = (min(a, b), max(a, b))
        if pair in seen:
            continue

        pa = pos[a]
        pb = pos[b]

        # もともと隣接していたらスキップ
        if pa[0] + 1 == pa[1] or pb[0] + 1 == pb[1]:
            continue

        v = [pa[0], pa[1], pb[0], pb[1]]
        v.sort()

        # 隣接条件のチェック
        if v[0] + 1 == v[1] and v[2] + 1 == v[3]:
            seen.add(pair)
            ans += 1

    print(ans)
