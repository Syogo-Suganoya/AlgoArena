N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

crr = 0
s = {0}  # 累積和を格納する集合（0も入れておく）

# 累積和を計算しながら集合に追加
for ai in A:
    crr += ai
    s.add(crr)

# すべての累積和 x に対して、x+p, x+p+q, x+p+q+r もあれば条件達成
for x in s:
    if x + P in s and x + P + Q in s and x + P + Q + R in s:
        print("Yes")
        break
else:
    print("No")
