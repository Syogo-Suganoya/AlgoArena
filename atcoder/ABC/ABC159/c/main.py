L = float(input())
# 最大体積 = (L/3)^3 = L^3 / 27
ans = (L**3) / 27
# 小数12桁で出力
print(f"{ans:.12f}")
