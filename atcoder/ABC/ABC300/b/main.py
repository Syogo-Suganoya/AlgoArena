H, W = map(int, input().split())
maze1 = [list(input()) for _ in range(H)]
maze2 = [list(input()) for _ in range(H)]


def shift_match():
    for i in range(H):  # 縦のシフト
        for j in range(W):  # 横のシフト
            shifted = [
                [maze1[(x - i) % H][(y - j) % W] for y in range(W)] for x in range(H)
            ]
            if shifted == maze2:
                return True
    return False


print("Yes" if shift_match() else "No")
