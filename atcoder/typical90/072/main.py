H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(sx, sy, px, py, used):
    # 始点に戻り、すでに訪問済みの場合はサイクルを検出
    if sx == px and sy == py and used[px][py]:
        return 0

    # 現在の位置を訪問済みに設定
    used[px][py] = True
    ret = -10000

    # 4方向に探索
    for i in range(4):
        nx, ny = px + dx[i], py + dy[i]
        # グリッド外、または山(`#`)ならスキップ
        if not (0 <= nx < H and 0 <= ny < W) or grid[nx][ny] == "#":
            continue
        # サイクルを形成していない訪問済みのマスならスキップ
        if (sx != nx or sy != ny) and used[nx][ny]:
            continue
        # 再帰的に探索
        v = dfs(sx, sy, nx, ny, used)
        ret = max(ret, v + 1)

    # 探索が終わったら現在の位置を未訪問に戻す（バックトラッキング）
    used[px][py] = False
    return ret


answer = -1
used = [[False] * W for _ in range(H)]

# 全ての平野(`.`)を始点として探索
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":
            answer = max(answer, dfs(i, j, i, j, used))

# サイクルが見つからなかった場合
if answer <= 2:
    answer = -1

print(answer)
