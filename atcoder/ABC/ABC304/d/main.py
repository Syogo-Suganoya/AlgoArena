import bisect
import collections

# ケーキの幅W、高さH
W, H = map(int, input().split())

# イチゴの数
N = int(input())

# 各イチゴの座標 (p, q)
pq = [list(map(int, input().split())) for _ in [0] * N]

# 横方向の切れ目の本数 A と位置
A = int(input())
a_list = [0, *list(map(int, input().split())), W]
# 0とWを両端に追加して「区画境界」として使う

# 縦方向の切れ目の本数 B と位置
B = int(input())
b_list = [0, *list(map(int, input().split())), H]
# 0とHを両端に追加

# 各区画ごとのイチゴの数をカウントする
count = collections.Counter()
for p, q in pq:
    # bisect_leftで「pが入る区間のインデックス」を求める
    # これが横方向の区画番号になる
    x_index = bisect.bisect_left(a_list, p)
    # 縦方向も同様
    y_index = bisect.bisect_left(b_list, q)
    # (横区画番号, 縦区画番号) をキーとしてカウント
    count[(x_index, y_index)] += 1

# 各区画に入ったイチゴ数の最小値と最大値を求める
minimum = min(count.values())
maximum = max(count.values())

# ただし、イチゴが全く入っていない区画がある場合、
# その区画のイチゴ数は0になるので、最小値を0に修正する
if len(count) < (A + 1) * (B + 1):
    minimum = 0

# 結果を出力
print(minimum, maximum)
