import math


# 内積計算用関数
def dot(ax, ay, bx, by):
    return ax * bx + ay * by


# 区間 [L,R] で f(t) = |B + C*t|^2 の最小値を求める関数
# B = (bx, by) 初期の相対位置ベクトル
# C = (cx, cy) 相対速度ベクトル
def min_quad_on_interval(bx, by, cx, cy, L, R):
    """二次関数 f(t) = |B + C*t|^2 の区間[L,R]での最小値を求める"""

    if L > R:
        return float("inf")  # 区間が不正なら無限大

    # tにおける距離の2乗
    def val(t):
        x = bx + cx * t
        y = by + cy * t
        return x * x + y * y  # 二乗のまま計算（sqrtは後で）

    # Cの大きさの2乗
    cc = dot(cx, cy, cx, cy)

    # 速度ベクトルがゼロなら、区間の端が最小
    if cc <= 1e-15:
        return min(val(L), val(R))

    # f(t) = |B + C*t|^2 の微分から t の最小点を計算
    bc = dot(bx, by, cx, cy)
    t0 = -bc / cc

    # t0が区間外なら端にクリップ
    if t0 < L:
        t0 = L
    elif t0 > R:
        t0 = R

    # 区間の端と頂点の値の中から最小を返す
    return min(val(L), val(R), val(t0))


# 各テストケースの処理
def solve(TSX, TSY, TGX, TGY, ASX, ASY, AGX, AGY):
    # 高橋君のスタートからゴールへのベクトル
    d1x, d1y = TGX - TSX, TGY - TSY
    T1 = math.hypot(d1x, d1y)  # 移動距離
    v1x, v1y = d1x / T1, d1y / T1  # 速度ベクトル（単位時間）

    # 青木君のスタートからゴールへのベクトル
    d2x, d2y = AGX - ASX, AGY - ASY
    T2 = math.hypot(d2x, d2y)
    v2x, v2y = d2x / T2, d2y / T2

    ans2 = float("inf")  # 最短距離の初期値

    # 時間区間ごとに最短距離を計算する
    # 1. 両者移動中の時間区間 [0, min(T1,T2)]
    stop_time_first = min(T1, T2)
    min_dist_sq_period1 = min_quad_on_interval(
        TSX - ASX, TSY - ASY, v1x - v2x, v1y - v2y, 0.0, stop_time_first
    )
    ans2 = min(ans2, min_dist_sq_period1)

    # 2. 片方だけが移動している時間区間
    if T1 < T2:
        # 高橋君がゴールに到達し停止している時間 [T1, T2]
        min_dist_sq_period2 = min_quad_on_interval(
            TGX - ASX, TGY - ASY, -v2x, -v2y, T1, T2
        )
        ans2 = min(ans2, min_dist_sq_period2)

    elif T2 < T1:
        # 青木君がゴールに到達し停止している時間 [T2, T1]
        min_dist_sq_period2 = min_quad_on_interval(
            TSX - AGX, TSY - AGY, v1x, v1y, T2, T1
        )
        ans2 = min(ans2, min_dist_sq_period2)

    # 3. 両者ともゴールに到達した場合（距離一定）
    final_dist_sq = (TGX - AGX) ** 2 + (TGY - AGY) ** 2
    ans2 = min(ans2, final_dist_sq)

    return math.sqrt(ans2)  # 二乗から平方根で距離を返す


# 入力処理
T = int(input())
out = []
for _ in range(T):
    TSX, TSY, TGX, TGY = map(int, input().split())
    ASX, ASY, AGX, AGY = map(int, input().split())
    ans = solve(TSX, TSY, TGX, TGY, ASX, ASY, AGX, AGY)
    out.append(f"{ans:.15f}")
print("\n".join(out))
