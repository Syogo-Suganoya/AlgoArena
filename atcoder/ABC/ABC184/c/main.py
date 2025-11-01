r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

p = abs(r2 - r1)
q = abs(c2 - c1)

# 0手で到達
if p == 0 and q == 0:
    print(0)
# 1手で到達
elif p == q or p + q <= 3:
    print(1)
# 2手で到達
elif (p + q) % 2 == 0 or p + q <= 6 or abs(p - q) <= 3:
    print(2)
# それ以外は3手
else:
    print(3)
