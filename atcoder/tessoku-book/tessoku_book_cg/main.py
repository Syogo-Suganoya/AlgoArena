N = int(input())

# 座標範囲に合わせた配列を用意
MAX = 1500
grid = [[0] * (MAX + 2) for _ in range(MAX + 2)]

# 点のプロット
for _ in range(N):
    X, Y = map(int, input().split())
    grid[X][Y] += 1  # 同じ座標に複数点があっても対応

# 二次元累積和の構築
# S[x][y] = (1,1)〜(x,y) の矩形内の点の個数
S = [[0] * (MAX + 2) for _ in range(MAX + 2)]
for x in range(1, MAX + 1):
    for y in range(1, MAX + 1):
        S[x][y] = (
            S[x - 1][y]  # 上の累積
            + S[x][y - 1]  # 左の累積
            - S[x - 1][y - 1]  # ダブルカウント修正
            + grid[x][y]  # 自分のマス
        )

# クエリ処理
Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    # (a,b)〜(c,d) の矩形内の個数を二次元累積和で取得
    ans = S[c][d] - S[a - 1][d] - S[c][b - 1] + S[a - 1][b - 1]
    print(ans)
