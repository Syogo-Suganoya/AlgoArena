# --- 外積を求める関数 ---
# 2つのベクトル A=(ax, ay), B=(bx, by) の外積を返す
# 外積 > 0 : BはAの左側にある
# 外積 < 0 : BはAの右側にある
# 外積 = 0 : AとBは一直線上
def gaiseki(A, B):
    return A[0] * B[1] - A[1] * B[0]


# --- 入力処理 ---
N = int(input())  # 多角形の頂点数
P = [
    tuple(map(int, input().split())) for _ in range(N)
]  # 多角形の頂点座標（順に与えられる）
sx, sy = map(int, input().split())  # 判定したい点の座標


cnt = 0  # 点から右方向に伸ばした線分と多角形の辺の交差回数

# --- 各辺を順番に確認 ---
for i in range(N):
    ax, ay = P[i]
    bx, by = P[(i + 1) % N]  # 最後の頂点と最初の頂点をつなぐ

    # 辺の端点を y の小さい順に並べる（処理を簡単にするため）
    if ay > by:
        ax, ay, bx, by = bx, by, ax, ay

    # 点 (sx, sy) を基準にしたベクトルに変換
    A = (ax - sx, ay - sy)
    B = (bx - sx, by - sy)

    # 条件：
    # 1. 点の y 座標 sy が辺の縦範囲 (ay, by] の中にある
    # 2. 外積が負 → 辺が点の右側にある（交差している）
    if ay < sy <= by and gaiseki(A, B) < 0:
        cnt += 1

# 交差回数が奇数なら点は多角形の内側、偶数なら外側
if cnt % 2 == 1:
    print("INSIDE")
else:
    print("OUTSIDE")
