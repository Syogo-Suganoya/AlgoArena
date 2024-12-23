# https://qiita.com/hyouri/items/c07ab3913d6864a4b348#d%E5%95%8F%E9%A1%8C

from collections import defaultdict

from sortedcontainers import SortedSet

n, m, i, j = map(int, input().split())
x = defaultdict(SortedSet)
y = defaultdict(SortedSet)

for _ in range(n):
    x_i, y_i = map(int, input().split())
    x[x_i].add(y_i)
    y[y_i].add(x_i)

ans = 0
for _ in range(m):
    d, C = input().split()
    c = int(C)
    if d == "U":
        lst = x[i].irange(j, j + c)
        data = [(i, l_i) for l_i in lst]
        j += c
    elif d == "D":
        lst = x[i].irange(j - c, j)
        data = [(i, l_i) for l_i in lst]
        j -= c
    elif d == "R":
        lst = y[j].irange(i, i + c)
        data = [(l_i, j) for l_i in lst]
        i += c
    else:
        lst = y[j].irange(i - c, i)
        data = [(l_i, j) for l_i in lst]
        i -= c

    ans += len(data)
    for x_i, y_i in data:
        x[x_i].discard(y_i)
        y[y_i].discard(x_i)

print(i, j, ans)
