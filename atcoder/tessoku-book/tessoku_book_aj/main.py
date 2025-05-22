N, K = map(int, input().split())

# 最短距離
min_steps = 2 * (N - 1)

# 距離が足りて、ゴール付近で調整できるか
if K >= min_steps and (K - min_steps) % 2 == 0:
    print("Yes")
else:
    print("No")
