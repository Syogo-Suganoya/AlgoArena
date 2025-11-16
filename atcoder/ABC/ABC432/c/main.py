N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


# 最小と最大で矛盾があれば -1
minA = min(A) * Y  # 大きい飴全部だったら A[i] * Y
maxA = max(A) * X  # 小さい飴全部だったら A[i] * X
# この範囲の中か
if not (minA >= maxA):
    print(-1)
    exit()

# 次に「Y - X」で刻まれた重さだけが変化するので、
# A[i] * X mod (Y - X) がすべて同じである必要がある。
mod = Y - X
rem0 = (A[0] * X) % mod
for a in A:
    if (a * X) % mod != rem0:
        print(-1)
        exit()

# “最も制約が厳しい人”の重さにあわせるのが最適
G = minA

# それぞれ i に対して t_i = (G − A[i] * X) ÷ (Y − X)
# を計算して「大きな飴の合計数」を求める。
total_t = 0
for a in A:
    total_t += (G - a * X) // mod

print(total_t)
