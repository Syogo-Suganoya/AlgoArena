# グリッドのサイズを入力
N, M = map(int, input().split())
# グリッドの内容を読み込む
grid = [input() for _ in range(N)]

# 各マスで「停止状態」で到達したかどうかを管理する2次元リスト
stopped = [[False] * M for _ in range(N)]
# 各マスで「通過状態」で到達したかどうかを管理する2次元リスト
passed = [[False] * M for _ in range(N)]


def dfs(i, j):
    # (i, j) に停止状態で到達
    stopped[i][j] = True
    # 4方向（右, 下, 左, 上）に対して探索
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i, j
        # 岩にぶつかるまで滑り続ける
        while grid[ni + di][nj + dj] != "#":
            ni += di
            nj += dj
            # 通過状態として記録
            passed[ni][nj] = True
        # 新たに停止状態で到達したマスがあれば再帰的に探索
        if not stopped[ni][nj]:
            dfs(ni, nj)


# スタート地点 (1,1) を通過状態にする
passed[1][1] = True
# (1,1) から深さ優先探索を開始
dfs(1, 1)

# 通過状態になったマスの総数をカウント
result = sum(sum(row) for row in passed)
print(result)
