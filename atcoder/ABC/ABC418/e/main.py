import math
from collections import Counter

N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]

# 総組み合わせ数 (4点選び) は C(N,4) だが、直接それを作って台形判定するのは O(N^4) で無理。
# アプローチ：
#   任意の 2点 (i,j) を線分とみて、その線分の“傾き（方向）”を確定。
#   同じ傾きを持つ別の線分を選ぶと平行な辺ができる → 台形の条件に近づく。
#
#   ただし平行四辺形（2組の平行辺）などは重複カウントされるので補正する必要あり。

# map: 傾き → 数
# map2: 傾き＋長さ → 数（平行四辺形補正用）
cnt_dir = Counter()
cnt_dir_len = Counter()

# 線分 (i,j) をすべて列挙
for i in range(N):
    x1, y1 = pts[i]
    for j in range(i + 1, N):
        x2, y2 = pts[j]
        dx = x2 - x1
        dy = y2 - y1

        # 傾きを dx,dy の比で整数化（符号・最大公約数で整える）
        if dx == 0:
            dir_key = ("inf", 0)  # 垂直な線
        elif dy == 0:
            dir_key = (0, "inf")  # 水平な線
        else:
            g = math.gcd(dx, dy)
            dx0 = dx // g
            dy0 = dy // g
            # 正規方向に統一（dy0 が負なら符号を反転させておく）
            if dy0 < 0:
                dx0 = -dx0
                dy0 = -dy0
            dir_key = (dy0, dx0)

        # 長さ（距離二乗）もキーに加えると平行四辺形用補正用
        length_sq = dx * dx + dy * dy

        cnt_dir[dir_key] += 1
        cnt_dir_len[(dir_key, length_sq)] += 1

# 平行な線分ペアの組み合わせ数をまず計算
total_parallel_pairs = 0
for v in cnt_dir.values():
    # v 個の線分から 2 本選ぶ組み合わせ
    total_parallel_pairs += v * (v - 1) // 2

# 次に、平行四辺形（＝同じ傾き かつ同じ長さの線分ペア）を重複カウントから補正
subtract_for_parallelograms = 0
for v in cnt_dir_len.values():
    subtract_for_parallelograms += v * (v - 1) // 2

# 台形の数 = 「平行線分ペア数」 − 「平行四辺形補正」／2
# ※平行四辺形は2組の平行線を使うので重複計上されている分を補正
result = total_parallel_pairs - subtract_for_parallelograms // 2

print(result)
