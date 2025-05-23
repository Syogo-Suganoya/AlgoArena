from collections import deque

# 入力の読み込み
N, X = map(int, input().split())
S = list(input())

# キューの初期化
queue = deque()
X -= 1  # 0-indexed に変換
queue.append(X)

# 青に塗る
S[X] = "@"

# BFS
while queue:
    pos = queue.popleft()
    for neighbor in [pos - 1, pos + 1]:
        if 0 <= neighbor < N and S[neighbor] == ".":
            S[neighbor] = "@"
            queue.append(neighbor)

# 結果の出力
print("".join(S))
