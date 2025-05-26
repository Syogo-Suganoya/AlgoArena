l = []
for i in range(3):
    x, y = map(int, input().split())
    l.append((x, y))


# 3つの辺の長さの2乗を計算
def squared_dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


# 辺の長さの2乗を計算
AB2 = squared_dist(l[0], l[1])
BC2 = squared_dist(l[1], l[2])
AC2 = squared_dist(l[0], l[2])

# 3つの辺の2乗をリスト化してソート
sides2 = sorted([AB2, BC2, AC2])

# 最も長い辺が斜辺、残り2つの和がそれと等しいかチェック
if sides2[0] + sides2[1] == sides2[2]:
    print("Yes")
else:
    print("No")
