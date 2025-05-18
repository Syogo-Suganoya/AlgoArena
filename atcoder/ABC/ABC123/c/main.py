import math

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

# ボトルネック
# 結局ここであと詰まりが起きる
min_capacity = min(A, B, C, D, E)

moves = math.ceil(N / min_capacity)
total_time = 5 + (moves - 1)

print(total_time)
