from sympy import divisors

N, M = map(int, input().split())

# 約数を降順で取得
divs = sorted(divisors(M), reverse=True)

# 最大の d を探す（降順なので最初に見つかったら即終了）
for d in divs:
    if d * N <= M:
        print(d)
        break
