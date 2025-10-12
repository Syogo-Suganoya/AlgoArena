from collections import deque

h, w = map(int, input().split())
a = [list(input().strip()) for _ in range(h)]

# スタート位置
px = py = -1
for i in range(h):
    for j in range(w):
        if a[i][j] == "T":
            px, py = i, j

# 累積和で黒マスの数を管理
s = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + (a[i][j] == "#")

# 6次元 DP を作成
inf = 10**9
d = [
    [
        [
            [[[inf] * (2 * w + 1) for _ in range(2 * h + 1)] for _ in range(w + 1)]
            for _ in range(w + 1)
        ]
        for _ in range(h + 1)
    ]
    for _ in range(h + 1)
]

# 初期状態
d[0][h][0][w][h][w] = 0
que = deque()
que.append((0, h, 0, w, h, w))

while que:
    lx, rx, ly, ry, xx, yy = que.popleft()

    # 現在の生きている黒マスが0なら終了
    total_black = s[rx][ry] + s[lx][ly] - s[lx][ry] - s[rx][ly]
    if total_black == 0:
        print(d[lx][rx][ly][ry][xx][yy])
        break

    # 4方向の移動
    for D in range(4):
        nlx, nrx, nly, nry, nxx, nyy = lx, rx, ly, ry, xx, yy
        if D == 0:
            nxx += 1
        elif D == 1:
            nxx -= 1
        elif D == 2:
            nyy += 1
        else:
            nyy -= 1

    # 移動後に生き残る黒マスの範囲を更新
    nlx = max(nlx, nxx - h)  # 左端は、Tの現在位置のx座標のオフセットより左にはできない
    nrx = min(nrx, nxx)  # 右端は、Tの現在位置のx座標を超えない
    nly = max(nly, nyy - w)  # 上端は、Tの現在位置のy座標のオフセットより上にはできない
    nry = min(nry, nyy)  # 下端は、Tの現在位置のy座標を超えない

    # Tの座標が迷路外に出ていれば無効
    if not (0 <= nxx <= 2 * h and 0 <= nyy <= 2 * w):
        continue

    # Tの現在位置を迷路上の絶対座標に変換
    X = px + nxx - h
    Y = py + nyy - w

    # 移動先が黒マスでまだ消滅していない場合は進めない
    if nlx <= X < nrx and nly <= Y < nry and a[X][Y] == "#":
        continue

    # この状態にまだ訪れていなければ距離を更新してキューに追加
    if d[nlx][nrx][nly][nry][nxx][nyy] == inf:
        d[nlx][nrx][nly][nry][nxx][nyy] = d[lx][rx][ly][ry][xx][yy] + 1
        que.append((nlx, nrx, nly, nry, nxx, nyy))
else:
    print(-1)
