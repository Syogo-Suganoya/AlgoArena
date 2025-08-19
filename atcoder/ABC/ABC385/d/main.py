def main():
    from collections import defaultdict

    from sortedcontainers import SortedSet

    n, m, Sx, Sy = map(int, input().split())

    # x[y] = {すべての x 座標}、y[x] = {すべての y 座標}
    x = defaultdict(SortedSet)
    y = defaultdict(SortedSet)

    # 座標を登録
    for _ in range(n):
        xi, yi = map(int, input().split())
        x[yi].add(xi)  # y 軸でまとめて x を格納
        y[xi].add(yi)  # x 軸でまとめて y を格納

    ans = 0  # 取得したポイントの総数
    cx, cy = Sx, Sy  # 現在位置

    # --- クエリ処理 ---
    for _ in range(m):
        D, C = input().split()
        C = int(C)

        if D == "L":  # 左へ C
            nx = cx - C
            s = x[cy]  # 同一直線 (y=cy) の x 坐標集合
            l = s.bisect_left(nx)  # nx 以上
            r = s.bisect_left(cx)  # cx 未満
            targets = list(s.islice(l, r))  # nx <= x < cx
            ans += len(targets)
            for xx in targets:  # 両辞書から削除
                s.discard(xx)
                y[xx].discard(cy)
            cx = nx

        elif D == "R":  # 右へ C
            nx = cx + C
            s = x[cy]
            l = s.bisect_right(cx)  # cx より大きい
            r = s.bisect_right(nx)  # nx 以下
            targets = list(s.islice(l, r))
            ans += len(targets)
            for xx in targets:
                s.discard(xx)
                y[xx].discard(cy)
            cx = nx

        elif D == "D":  # 下へ C
            ny = cy - C
            s = y[cx]
            l = s.bisect_left(ny)
            r = s.bisect_left(cy)
            targets = list(s.islice(l, r))  # ny <= y < cy
            ans += len(targets)
            for yy in targets:
                s.discard(yy)
                x[yy].discard(cx)
            cy = ny

        elif D == "U":  # 上へ C
            ny = cy + C
            s = y[cx]
            l = s.bisect_right(cy)
            r = s.bisect_right(ny)
            targets = list(s.islice(l, r))  # cy < y <= ny
            ans += len(targets)
            for yy in targets:
                s.discard(yy)
                x[yy].discard(cx)
            cy = ny

    print(cx, cy, ans)


main()
