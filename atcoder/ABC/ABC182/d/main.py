N = int(input())
A = list(map(int, input().split()))

"""
- 累積和 (prefix sum): 各ステップでの移動距離を計算するために、A の累積和を求めます。
- 最大値の追跡: 各ステップでの累積和の最大値を追跡し、ロボットが到達可能な最大座標を更新していきます。

cumulative_sum で現在までの累積和を計算し、
max_cumulative でその最大値を保持します。

current_pos はロボットの現在の座標を示し、
各ステップで current_pos + max_cumulative を計算して max_pos を更新します。
"""

max_pos = 0  # ロボットが到達した最大座標
current_pos = 0  # 現在の座標
cumulative_sum = 0  # 累積和
max_cumulative = 0  # 累積和の最大値

for a in A:
    cumulative_sum += a
    max_cumulative = max(max_cumulative, cumulative_sum)
    max_pos = max(max_pos, current_pos + max_cumulative)
    current_pos += cumulative_sum

print(max_pos)
