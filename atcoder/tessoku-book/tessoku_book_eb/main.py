from sortedcontainers import SortedSet

N = int(input())
s = SortedSet()  # 昇順に保持できる集合（重複なし）

for _ in range(N):
    q, c = map(int, input().split())

    if q == 1:
        # 値を追加（重複は自動で除外される）
        s.add(c)

    elif q == 2:
        if len(s) == 0:
            # 要素が無い場合は -1
            print(-1)
            continue

        # 位置を二分探索
        idx = s.bisect_left(c)

        candidates = []
        if idx > 0:
            candidates.append(abs(s[idx - 1] - c))
        if idx < len(s):
            candidates.append(abs(s[idx] - c))

        print(min(candidates))
