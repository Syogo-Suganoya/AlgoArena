from sortedcontainers import SortedList

n, d = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

# 番兵を入れておく（境界チェック不要にするため）
s = SortedList([-(10**18), 10**18])

r = 0

for l in range(n):
    while r < n:
        x = a[r]

        # lower_bound 相当
        pos = s.bisect_left(x)

        # 右側チェック
        if s[pos] - x < d:
            break

        # 左側チェック
        if x - s[pos - 1] < d:
            break

        s.add(x)
        r += 1

    ans += r - l

    # 削除（C++ の erase 相当）
    s.remove(a[l])

print(ans)
