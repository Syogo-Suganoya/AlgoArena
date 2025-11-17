from collections import defaultdict

H, W, N = map(int, input().split())

# 各行・列にあるゴミの位置を記録
rows = defaultdict(list)
cols = defaultdict(list)
garbage = []  # ゴミの座標を覚えておく（削除時に使う）

for i in range(N):
    x, y = map(int, input().split())
    rows[x].append((i, y))
    cols[y].append((i, x))
    garbage.append((x, y))

# 各ゴミがまだ残っているか
alive = [True] * N
# 行と列がすでに処理済みか
row_removed = [False] * (H + 1)
col_removed = [False] * (W + 1)

Q = int(input())

for _ in range(Q):
    t, idx = map(int, input().split())

    # 行の削除
    if t == 1:
        if row_removed[idx]:
            print(0)
            continue

        cnt = 0
        for gid, y in rows[idx]:
            if alive[gid]:
                alive[gid] = False
                cnt += 1
        row_removed[idx] = True
        print(cnt)

    # 列の削除
    else:
        if col_removed[idx]:
            print(0)
            continue

        cnt = 0
        for gid, x in cols[idx]:
            if alive[gid]:
                alive[gid] = False
                cnt += 1
        col_removed[idx] = True
        print(cnt)
