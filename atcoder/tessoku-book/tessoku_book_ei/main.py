from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1] * (N + 1)
parent[1] = 0  # スタート地点（1）の親は 0 とする
queue = deque([1])

while queue:
    v = queue.popleft()
    for u in graph[v]:
        if parent[u] == -1:  # 未訪問であれば
            parent[u] = v
            queue.append(u)

# 頂点 N へのパス復元
path = []
cur = N
while cur != 0:
    path.append(cur)
    cur = parent[cur]
path.reverse()

print(*path)
