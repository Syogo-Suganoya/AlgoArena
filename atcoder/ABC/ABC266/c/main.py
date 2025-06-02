from itertools import combinations


# 2つのベクトルの外積（2次元なので、スカラー値が返る）
def cross(ax, ay, bx, by):
    return ax * by - ay * bx


# 点が凸多角形を形成できるかどうかを判定
def is_convex(p):
    # 4点から3点を選ぶ組み合わせをすべて調べる
    for i1, i2, i3 in combinations(range(4), 3):
        x1, y1 = p[i1]
        x2, y2 = p[i2]
        x3, y3 = p[i3]

        # ベクトルを作成
        vx1, vy1 = x2 - x1, y2 - y1
        vx2, vy2 = x3 - x2, y3 - y2

        # 外積で角度を調べる（符号が変わると内角が180度以上になる）
        if cross(vx1, vy1, vx2, vy2) <= 0:
            return False  # 1つでも凹角があれば凸多角形じゃない
    return True


X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())
X4, Y4 = map(int, input().split())

# 4つの点の座標をリスト化
points = [(X1, Y1), (X2, Y2), (X3, Y3), (X4, Y4)]

print("Yes" if is_convex(points) else "No")
