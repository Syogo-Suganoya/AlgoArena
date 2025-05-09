H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]


def main():
    # snukeの文字列と8方向（上下左右＋斜め）
    target = "snuke"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(H):
        for j in range(W):
            if maze[i][j] != "s":
                continue
            for dx, dy in directions:
                pos = []
                for k in range(5):
                    ni = i + dx * k
                    nj = j + dy * k
                    if not (0 <= ni < H and 0 <= nj < W):
                        break
                    if maze[ni][nj] != target[k]:
                        break
                    pos.append((ni + 1, nj + 1))  # 1-indexed
                if len(pos) == 5:
                    return pos


for i in main():
    print(*i)
