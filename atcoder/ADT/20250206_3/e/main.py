x1, y1, x2, y2 = map(int, input().split())


def main():
    directions = [
        (2, 1),
        (1, 2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (1, -2),
        (-2, -1),
        (-1, -2),
    ]
    # x1, y1 の 8 方向の座標を取得
    reachable_from_start = {(x1 + dx, y1 + dy) for dx, dy in directions}
    # x2, y2 の 8 方向の座標を確認
    for dx, dy in directions:
        if (x2 + dx, y2 + dy) in reachable_from_start:
            return True
    return False


print("Yes" if main() else "No")
