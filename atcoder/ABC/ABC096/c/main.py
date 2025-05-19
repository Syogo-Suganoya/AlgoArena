H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# 4方向の移動（上, 下, 左, 右）
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":
            continue

        # 黒マスが見つかったら周囲4マスを確認
        isolated = True
        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            # 範囲内かつ隣が黒マスなら孤立していない
            if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == "#":
                isolated = False
                break

        if isolated:
            print("No")
            exit()

print("Yes")
