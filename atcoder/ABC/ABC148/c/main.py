import math

# 入力
N, M = map(int, input().split())

# 最小公倍数を計算
result = math.lcm(N, M)  # Python 3.9+ で使用可能

# 出力
print(result)
