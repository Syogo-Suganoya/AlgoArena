import math

# 入力
Xf, Yf, Rf = map(float, input().split())

SCALE = 10000  # 小数を整数化するスケール
Xi = round(Xf * SCALE)
Yi = round(Yf * SCALE)
Ri = round(Rf * SCALE)


# 整数平方根を安全に求める関数
def integer_sqrt(n):
    return int(math.isqrt(n))


# x を整数座標に変換してループ
# x_min から x_max の範囲を整数で
x_min = (Xi - Ri + SCALE - 1) // SCALE
x_max = (Xi + Ri) // SCALE

ans = 0
for x in range(x_min, x_max + 1):
    # 円の式から y の範囲を求める
    dx = Xi - x * SCALE
    if dx * dx > Ri * Ri:
        continue
    dy2 = Ri * Ri - dx * dx
    dy = integer_sqrt(dy2)

    y_low = (Yi - dy + SCALE - 1) // SCALE
    y_high = (Yi + dy) // SCALE
    ans += max(0, y_high - y_low + 1)

print(ans)
