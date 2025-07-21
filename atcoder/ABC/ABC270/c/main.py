from collections import deque

n, x, y = map(int, input().split())
U = [0] * (n - 1)
V = [0] * (n - 1)

# グラフ作成（無向グラフ）
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFSで親を記録
parent = [-1] * (n + 1)
queue = deque()
queue.append(x)
parent[x] = 0  # 探索済みマーク（0とかNone以外ならなんでもOK）

while queue:
    v = queue.popleft()
    for nv in graph[v]:
        if parent[nv] == -1:
            parent[nv] = v
            queue.append(nv)

# パス復元
path = []
cur = y
while cur != 0:
    path.append(cur)
    cur = parent[cur]

path.reverse()
print(*path)
