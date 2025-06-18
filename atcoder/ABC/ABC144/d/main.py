import math

a, b, x = map(int, input().split())
V = a * a * b  # 容器全体の体積

if x <= V / 2:
    # 水が少なめ→断面は三角形
    # tan(θ) = (a * b^2) / (2 * x)
    θ = math.atan((a * b * b) / (2 * x))
else:
    # 水が多め→空間が三角形
    # tan(θ) = (2 * (a^2*b - x)) / (a^3)
    θ = math.atan((2 * (V - x)) / (a**3))

# ラジアンを度に直す
print(math.degrees(θ))
