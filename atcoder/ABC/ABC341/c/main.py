H, W, N = map(int, input().split())
T = input()
maze = [list(input()) for _ in range(H)]

# 移動方向の辞書
dir = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

res = 0

# すべてのマスを試す
for si in range(H):
    for sj in range(W):
        if maze[si][sj] == "#":
            continue  # 最初から壁なら無理

        i, j = si, sj
        ok = True
        for move in T:
            di, dj = dir[move]
            ni, nj = i + di, j + dj

            # 範囲外 or 壁にぶつかったら終了
            if not (0 <= ni < H and 0 <= nj < W) or maze[ni][nj] == "#":
                ok = False
                break

            i, j = ni, nj

        if ok:
            res += 1

print(res)
