from collections import defaultdict, deque

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 各文字の位置リストを作る（'a'..'z'）
pos = defaultdict(list)
start = goal = None
for i in range(H):
    for j in range(W):
        ch = grid[i][j]
        if ch == "S":
            start = (i, j)
        elif ch == "G":
            goal = (i, j)
        elif ch != "." and ch != "#":
            pos[ch].append((i, j))

INF = 10**9
dist = [[INF] * W for _ in range(H)]
dq = deque()

# BFS 初期化
si, sj = start
dist[si][sj] = 0
dq.append((si, sj))

used = {
    chr(ord("a") + k): False for k in range(26)
}  # ある文字グループを一度だけ展開するため

# 4方向移動のための delta
d4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dq:
    i, j = dq.popleft()
    d = dist[i][j]
    # 隣接4方向
    for di, dj in d4:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] != "#" and dist[ni][nj] == INF:
            dist[ni][nj] = d + 1
            dq.append((ni, nj))

    # テレポート（同じ小文字の全マスへ）
    ch = grid[i][j]
    if ch >= "a" and ch <= "z" and not used[ch]:
        # この文字の全マスを距離 d+1 で一気にキューに追加
        for pi, pj in pos[ch]:
            if dist[pi][pj] == INF:
                dist[pi][pj] = d + 1
                dq.append((pi, pj))
        used[ch] = True  # 二度展開しない

gi, gj = goal
print(dist[gi][gj] if dist[gi][gj] != INF else -1)
