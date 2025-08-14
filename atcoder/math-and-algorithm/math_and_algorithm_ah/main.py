def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def dot(ax, ay, bx, by):
    return ax * bx + ay * by


def on_segment(px, py, ax, ay, bx, by):
    # 点 P が線分 AB 上にあるか 判定
    return (
        cross(bx - ax, by - ay, px - ax, py - ay) == 0
        and dot(px - ax, py - ay, px - bx, py - by) <= 0
    )


def segments_intersect(a, b, c, d):
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d

    # 外積による向きの判定
    c1 = cross(bx - ax, by - ay, cx - ax, cy - ay)
    c2 = cross(bx - ax, by - ay, dx - ax, dy - ay)
    c3 = cross(dx - cx, dy - cy, ax - cx, ay - cy)
    c4 = cross(dx - cx, dy - cy, bx - cx, by - cy)

    if c1 * c2 < 0 and c3 * c4 < 0:
        return True
    # 端点の重なりも OK
    if on_segment(ax, ay, cx, cy, dx, dy):
        return True
    if on_segment(bx, by, cx, cy, dx, dy):
        return True
    if on_segment(cx, cy, ax, ay, bx, by):
        return True
    if on_segment(dx, dy, ax, ay, bx, by):
        return True
    return False


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

if segments_intersect((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
    print("Yes")
else:
    print("No")
