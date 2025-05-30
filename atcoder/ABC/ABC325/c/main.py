H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

group = [[0] * W for _ in range(H)]
res = 1

for i in range(H):
    for j in range(W):
        if maze[i][j] == "#" and group[i][j] == 0:
            # スタック初期化
            stack = [(i, j)]
            group[i][j] = res
            while stack:
                ci, cj = stack.pop()
                # 周囲8方向1マスをスタック
                for dx, dy in dxdy:
                    ni, nj = ci + dx, cj + dy
                    if 0 <= ni < H and 0 <= nj < W:
                        # 未訪問のマスは、同じグループにする
                        if maze[ni][nj] == "#" and group[ni][nj] == 0:
                            group[ni][nj] = res
                            # 派生先も同じグループにする
                            stack.append((ni, nj))
            # スタックを消化しきったら、インクリメント
            res += 1

print(res - 1)
