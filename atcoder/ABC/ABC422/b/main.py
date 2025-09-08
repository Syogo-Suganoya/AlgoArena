H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]


def main():
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(H):
        for j in range(W):
            if maze[i][j] == ".":
                continue

            cnt = 0
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < H and 0 <= nj < W:
                    if maze[ni][nj] == "#":
                        cnt += 1

            if cnt != 2 and cnt != 4:
                return False
    return True


print("Yes" if main() else "No")
