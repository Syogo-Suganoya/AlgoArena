H, W, K = map(int, input().split())  # グリッド縦 H, 横 W, 歩数 K
grid = [input().strip() for _ in range(H)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# ————————————————————————————
# DFS で長さ K の「単純パス」を数える
# 単純パス: 同じマスを 2 回以上踏まない
# state = (y, x, step)
# step==K になったら 1 経路カウント
# ————————————————————————————
visited = [[False] * W for _ in range(H)]  # 再訪を禁止するためのフラグ


def dfs(y: int, x: int, step: int) -> int:
    """(y,x) から残り K-step 歩で行ける単純パスの本数を返す"""
    if step == K:  # 目的の長さに達した
        return 1  # 1 パターン発見
    cnt = 0
    for dir in range(4):  # 4 方向へ
        ny, nx = y + dy[dir], x + dx[dir]
        # グリッド内 && 通れるマス && 未訪問
        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] == "." and not visited[ny][nx]:
            visited[ny][nx] = True  # 行き先を訪問済みにして
            cnt += dfs(ny, nx, step + 1)  # 再帰（深く探索）
            visited[ny][nx] = False  # 帰ってきたら未訪問に戻す（バックトラック）
    return cnt


# ————————————————————————————
# すべての白マス ('.') をスタートに DFS
# 各スタートごとに訪問フラグを独立に扱う
# ————————————————————————————
answer = 0
for sy in range(H):
    for sx in range(W):
        if grid[sy][sx] == ".":
            visited[sy][sx] = True  # スタートを訪問済みにする
            answer += dfs(sy, sx, 0)  # 長さ 0 から探索
            visited[sy][sx] = False  # 次のスタートへ向けて初期化

print(answer)
