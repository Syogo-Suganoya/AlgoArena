from collections import deque, namedtuple

# path_info の構造体に相当
PathInfo = namedtuple("PathInfo", ["from_node", "to_node", "dist"])

# 入力
n, m = map(int, input().split())

# 無向グラフの隣接リスト
e = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1  # 0-indexed
    v -= 1
    e[u].append(v)
    e[v].append(u)

# ノード情報
s = input().strip()

# f[i][0], f[i][1]: ノード i に到達した最初と2番目の S の始点
# d[i][0], d[i][1]: それぞれの距離
f = [[-1, -1] for _ in range(n)]
d = [[-1, -1] for _ in range(n)]

q = deque()

# S からの BFS を初期化
for i in range(n):
    if s[i] == "S":
        f[i][0] = i
        d[i][0] = 0
        q.append(PathInfo(i, i, 0))

# BFS
while q:
    tmp = q.popleft()
    u = tmp.from_node
    v = tmp.to_node

    for nxt in e[v]:
        # まだ 1 回も到達していない場合
        if f[nxt][0] == -1:
            f[nxt][0] = u
            d[nxt][0] = tmp.dist + 1
            q.append(PathInfo(u, nxt, tmp.dist + 1))
        # 2 回目の到達（異なる始点からの到達）
        elif f[nxt][1] == -1 and f[nxt][0] != u:
            f[nxt][1] = u
            d[nxt][1] = tmp.dist + 1
            q.append(PathInfo(u, nxt, tmp.dist + 1))

# D ノードに対して距離の合計を出力
for i in range(n):
    if s[i] == "D":
        print(d[i][0] + d[i][1])
