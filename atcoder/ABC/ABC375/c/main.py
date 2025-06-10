n = int(input())
a = [list(input()) for _ in range(n)]

# 回転後の結果を格納するための空のグリッドを用意
ans = [[""] * n for _ in range(n)]

# 各マス (i, j) に対して回転後の位置を求める
for i in range(n):
    for j in range(n):
        # このマスが属するレイヤー（外側から何番目か）を計算
        # レイヤー番号は外から何段目か。1-indexed のため +1
        d = min(i + 1, j + 1, n - i, n - j)

        # 回転先の座標を初期化（最初は元の座標）
        ni, nj = i, j

        # d を 4 で割った余り（= 回転回数）だけ 90° 時計回りに回転
        for _ in range(d % 4):
            # 90度時計回りの回転 (i, j) → (j, n-1-i)
            ni, nj = nj, n - 1 - ni

        # 回転後の座標に文字を格納
        ans[ni][nj] = a[i][j]

# 回転後のグリッドを出力
for row in ans:
    print("".join(row))
