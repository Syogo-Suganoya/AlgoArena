import itertools
import math


# 二点間のユークリッド距離を計算する関数
def dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.hypot(dx, dy)


# 入力処理
N, S, T = map(int, input().split())
segments = []
for _ in range(N):
    A, B, C, D = map(int, input().split())
    # 線分の両端の座標をタプルで格納
    segments.append(((A, B), (C, D)))

# 最小時間の初期化（大きな値にしておく）
res = float("inf")

# 線分の全順列を試す（N!通り）
for perm in itertools.permutations(segments):
    # 各線分の方向（正向き or 逆向き）を2進数で管理（2^N通り）
    for flip_bits in range(1 << N):
        time = 0.0  # 今回の組み合わせでの移動時間
        now = (0, 0)  # 現在の位置（最初は原点）

        for i in range(N):
            # ビットで線分の方向を決める
            if (flip_bits >> i) & 1:
                from_, to_ = perm[i][1], perm[i][0]  # 逆向きに印字
            else:
                from_, to_ = perm[i][0], perm[i][1]  # 正向きに印字

            # 今の位置から印字開始点までの移動は通常移動速度 S
            time += dist(now, from_) / S
            # 印字中は印字移動速度 T
            time += dist(from_, to_) / T
            # 位置を更新
            now = to_

        # 最小時間を更新
        res = min(res, time)

# 結果を小数点以下12桁で出力
print("{:.12f}".format(res))
