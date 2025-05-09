def find_corners(maze):
    """
    黒で塗られたセル（#）の最も左上、右上、左下、右下の座標を求める関数
    """
    H, W = len(maze), len(maze[0])
    top, left, bottom, right = H, W, -1, -1

    for i in range(H):
        for j in range(W):
            if maze[i][j] == "#":
                # 左上
                top = min(top, i)
                left = min(left, j)
                # 右下
                bottom = max(bottom, i)
                right = max(right, j)

    # 左上、右上、左下、右下
    top_left = (top, left)
    top_right = (top, right)
    bottom_left = (bottom, left)
    bottom_right = (bottom, right)

    return top_left, top_right, bottom_left, bottom_right


def is_filled_rectangle(maze, top_left, bottom_right):
    top, left = top_left
    bottom, right = bottom_right

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if maze[i][j] == ".":
                return False
    return True


# 入力処理
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]


def main():
    # 隅を探す
    top_left, _, _, bottom_right = find_corners(maze)

    top, left = top_left
    bottom, right = bottom_right

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if maze[i][j] == ".":
                return i + 1, j + 1


print(*main())
