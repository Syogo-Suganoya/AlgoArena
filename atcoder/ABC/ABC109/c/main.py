import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 差分のリスト
diffs = [abs(a - M) for a in A]

# diffs の全体の gcd を求める
g = diffs[0]
for d in diffs[1:]:
    g = math.gcd(g, d)

print(g)
