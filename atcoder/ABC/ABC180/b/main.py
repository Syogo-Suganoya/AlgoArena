import math

N = int(input())
x = list(map(int, input().split()))

# L1ノルム（マンハッタン距離）
manhattan = sum(abs(xi) for xi in x)

# L2ノルム（ユークリッド距離）
euclidean = math.sqrt(sum(xi**2 for xi in x))

# L∞ノルム（チェビシェフ距離）
chebyshev = max(abs(xi) for xi in x)

# 出力
print(manhattan)
print(euclidean)
print(chebyshev)
