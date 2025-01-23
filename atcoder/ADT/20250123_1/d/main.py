H, W, D = map(int, input().split())  # 迷路の縦と横のサイズ
maze = [list(input()) for _ in range(H)]

res = 0


def f(h1, h2):
    res = 0
    for i in range(H):
        for j in range(W):
            if maze[i][j] != ".":
                continue
            d1 = abs(i - h1[0]) + abs(j - h1[1])
            if d1 <= D:
                res += 1
                continue
            d2 = abs(i - h2[0]) + abs(j - h2[1])
            if d2 <= D:
                res += 1
    return res


for i in range(H):
    for j in range(W):
        if maze[i][j] != ".":
            continue
        for i2 in range(H):
            for j2 in range(W):
                if maze[i2][j2] != ".":
                    continue
                res = max(res, f((i, j), (i2, j2)))

print(res)
