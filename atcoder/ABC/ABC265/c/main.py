import sys

sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]

# 訪問済みを管理
visited = [[False] * W for _ in range(H)]

# 移動方向
move = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def dfs(i, j):
    if visited[i][j]:
        # 一度訪れたマスに再訪 → 無限ループ
        print(-1)
        exit()
    visited[i][j] = True

    d = G[i][j]
    di, dj = move[d]
    ni, nj = i + di, j + dj

    # 範囲外に出る or 壁にぶつかるなら終了
    if not (0 <= ni < H and 0 <= nj < W):
        print(i + 1, j + 1)
        exit()

    dfs(ni, nj)


# スタート地点は (1,1) → インデックスは (0,0)
dfs(0, 0)
