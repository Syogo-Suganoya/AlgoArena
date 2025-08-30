N, Q = map(int, input().split())
P = [input().strip() for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# --------------------------
# 1. N x N パターンの二次元累積和を作成
#    g[i][j] = (0,0) から (i-1,j-1) までの黒マス数
# --------------------------
g = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        g[i][j] = (
            g[i - 1][j]
            + g[i][j - 1]
            - g[i - 1][j - 1]
            + (1 if P[i - 1][j - 1] == "B" else 0)
        )


# --------------------------
# 2. 長方形内の黒マス数を計算する関数
#    左上(0,0)から右下(x-1,y-1)までの黒マス
# --------------------------
def count_black(x, y):
    # x,y はパターン内の座標（0~N-1）
    # 累積和は 1-indexed に合わせる
    return g[x][y]


# --------------------------
# 3. クエリ処理
# --------------------------
for A, B, C, D in queries:
    # 長方形のサイズ
    H = C - A + 1
    W = D - B + 1

    # パターンの商と余り
    Aq, Ar = divmod(A, N)
    Bq, Br = divmod(B, N)
    Cq, Cr = divmod(C + 1, N)
    Dq, Dr = divmod(D + 1, N)

    # ① パターン全体の繰り返し分
    full_blocks = (Cq - Aq) * (Dq - Bq) * g[N][N]

    # ② 端の余り部分
    # 横端
    right_edge = (Cq - Aq) * count_black(N, Dr) - (Cq - Aq) * count_black(N, Br)
    # 縦端
    bottom_edge = (Dq - Bq) * count_black(Cr, N) - (Dq - Bq) * count_black(Ar, N)
    # 角の重複部分を引く
    corner = (
        count_black(Cr, Dr)  # 右下
        - count_black(Cr, Br)  # 左下
        - count_black(Ar, Dr)  # 右上
        + count_black(Ar, Br)  # 左上
    )

    ans = full_blocks + right_edge + bottom_edge + corner
    print(ans)
