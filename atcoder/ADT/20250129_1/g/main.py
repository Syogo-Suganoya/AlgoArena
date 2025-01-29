from collections import deque

# 入力の読み込み
h, w = map(int, input().split())  # 行数 h と列数 w
s = [input() for _ in range(h)]  # 迷路のマップ

# 移動方向 (右, 下, 上, 左)
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 目標となる文字列 "snuke"
target = "snuke"

# BFSのためのキュー
q = deque()

# スタート地点 (0, 0) から探索開始。k は現在の文字列の位置を表す (snuke のどの文字か)
q.append((0, 0, 0))  # (x, y, snuke の文字列のインデックス)

# 訪問済み地点の記録
visited = {}

# BFS開始
while q:
    x, y, k = q.popleft()

    # 現在の地点が目標文字列の次の文字か確認
    if s[x][y] != target[k % 5]:
        continue

    # すでに訪問した地点ならスキップ
    if (x, y) in visited:
        continue

    # 訪問済みとして記録
    visited[(x, y)] = 1

    # ゴール地点に到達した場合、Yes と出力して終了
    if (x, y) == (h - 1, w - 1):
        print("Yes")
        exit()

    # 4方向に移動して探索
    for direction in d:
        u, v = x + direction[0], y + direction[1]

        # 範囲内かつ次の文字が合っているか確認
        if 0 <= u < h and 0 <= v < w and s[u][v] == target[(k + 1) % 5]:
            q.append((u, v, k + 1))  # 次の文字に進む

# ゴールに到達できなかった場合、No と出力
print("No")
