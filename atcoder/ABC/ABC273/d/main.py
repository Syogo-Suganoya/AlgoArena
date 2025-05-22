import bisect
import sys
from collections import defaultdict

sys.setrecursionlimit(1 << 25)

H, W, rs, cs = map(int, input().split())
N = int(input())

# 壁の位置を行ごと、列ごとに管理
wall_row = defaultdict(list)
wall_col = defaultdict(list)

for _ in range(N):
    r, c = map(int, input().split())
    wall_row[r].append(c)
    wall_col[c].append(r)

# 各行・列の壁の位置をソートし、番兵を追加
for r in wall_row:
    wall_row[r].extend([0, W + 1])
    wall_row[r].sort()
for c in wall_col:
    wall_col[c].extend([0, H + 1])
    wall_col[c].sort()

Q = int(input())
curr_r, curr_c = rs, cs

for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == "L":
        row = wall_row.get(curr_r, [0, W + 1])
        idx = bisect.bisect_left(row, curr_c)
        wall = row[idx - 1]
        curr_c = max(curr_c - l, wall + 1)
    elif d == "R":
        row = wall_row.get(curr_r, [0, W + 1])
        idx = bisect.bisect_right(row, curr_c)
        wall = row[idx]
        curr_c = min(curr_c + l, wall - 1)
    elif d == "U":
        col = wall_col.get(curr_c, [0, H + 1])
        idx = bisect.bisect_left(col, curr_r)
        wall = col[idx - 1]
        curr_r = max(curr_r - l, wall + 1)
    elif d == "D":
        col = wall_col.get(curr_c, [0, H + 1])
        idx = bisect.bisect_right(col, curr_r)
        wall = col[idx]
        curr_r = min(curr_r + l, wall - 1)
    print(curr_r, curr_c)
