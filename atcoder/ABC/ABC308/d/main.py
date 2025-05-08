import sys

sys.setrecursionlimit(10**6)  # 再帰の深さ制限を緩和（最大10^6まで）


# DFS（深さ優先探索）
def dfs(t, x, y):
    if x == H - 1 and y == W - 1:
        # ゴールに到達したら "Yes" を出力して終了
        print("Yes")
        exit()

    visited[x][y] = True  # 現在地を訪問済みにする

    for dx, dy in dxy:  # 上下左右に移動を試す
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue  # 範囲外ならスキップ

        # まだ訪問しておらず、次の文字が一致していればDFSを続行
        if not visited[nx][ny] and S[nx][ny] == name[t]:
            dfs((t + 1) % 5, nx, ny)  # 次の文字へ（循環）


# 入力
H, W = map(int, input().split())
S = [input() for _ in range(H)]  # グリッド状の文字列入力

# 初期化
visited = [[0] * W for _ in range(H)]
name = "snuke"  # 探索する文字列
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 移動方向（右・左・下・上）

# スタート地点が 's' であればDFSを開始
if S[0][0] == "s":
    dfs(1, 0, 0)  # 次に期待する文字は 'n'

# ゴールできなかった場合
print("No")
