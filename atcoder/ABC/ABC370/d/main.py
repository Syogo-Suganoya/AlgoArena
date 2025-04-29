from sortedcontainers import SortedSet

# H: 行数, W: 列数, Q: クエリ数
H, W, Q = map(int, input().split())

# 各行・列において、どの位置に壁があるかを SortedSet で管理
Rs = [SortedSet() for _ in range(H)]  # Rs[i] は行iの壁がある列番号の集合
Cs = [SortedSet() for _ in range(W)]  # Cs[j] は列jの壁がある行番号の集合

# 各爆弾の処理
for _ in range(Q):
    R, C = map(int, input().split())
    R -= 1
    C -= 1

    # 壁がないなら、爆弾を設置（= 壁を追加）
    if C not in Rs[R]:
        Rs[R].add(C)
        Cs[C].add(R)
    else:
        # 壁がある場所に爆弾が来た → 周囲に波及する
        ric = Rs[R].bisect_left(C)
        cir = Cs[C].bisect_left(R)

        # -----------------------
        # 横方向（行）への爆発
        # -----------------------
        add_R = []

        # 左側を二分探索で確認（等差が保たれている間は「直線状に壁が続く」と判定）
        le = -1
        ri = ric
        while le + 1 < ri:
            mi = (le + ri) // 2
            if C - Rs[R][mi] == ric - mi:
                ri = mi
            else:
                le = mi
        if Rs[R][ri] > 0:
            add_R.append(Rs[R][ri] - 1)

        # 右側を二分探索で確認
        le = ric
        ri = len(Rs[R])
        while le + 1 < ri:
            mi = (le + ri) // 2
            if Rs[R][mi] - C == mi - ric:
                le = mi
            else:
                ri = mi
        if Rs[R][le] < W - 1:
            add_R.append(Rs[R][le] + 1)

        # -----------------------
        # 縦方向（列）への爆発
        # -----------------------
        add_C = []

        # 上方向を確認
        le = -1
        ri = cir
        while le + 1 < ri:
            mi = (le + ri) // 2
            if R - Cs[C][mi] == cir - mi:
                ri = mi
            else:
                le = mi
        if Cs[C][ri] > 0:
            add_C.append(Cs[C][ri] - 1)

        # 下方向を確認
        le = cir
        ri = len(Cs[C])
        while le + 1 < ri:
            mi = (le + ri) // 2
            if Cs[C][mi] - R == mi - cir:
                le = mi
            else:
                ri = mi
        if Cs[C][le] < H - 1:
            add_C.append(Cs[C][le] + 1)

        # 横方向の波及で新たに壁を追加
        for c in add_R:
            Rs[R].add(c)
            Cs[c].add(R)

        # 縦方向の波及で新たに壁を追加
        for r in add_C:
            Rs[r].add(C)
            Cs[C].add(r)

# 全マス H*W から壁があるマスを引く
ans = H * W
for i in range(H):
    ans -= len(Rs[i])
print(ans)
