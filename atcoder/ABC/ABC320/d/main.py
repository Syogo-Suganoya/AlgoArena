from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1  # 0-indexed
    B -= 1
    graph[A].append((B, X, Y))  # A → B に (X, Y)
    graph[B].append((A, -X, -Y))  # B → A に (-X, -Y)

# 座標の記録。None はまだ未確定。
res = [None] * N
res[0] = (0, 0)  # ノード1の座標を(0,0)とする

# BFSで座標を伝播
q = deque([0])
while q:
    u = q.popleft()
    ux, uy = res[u]
    for v, dx, dy in graph[u]:
        if res[v] is None:
            res[v] = (ux + dx, uy + dy)
            q.append(v)

# 出力
for r in res:
    if r is None:
        print("undecidable")
    else:
        print(*r)
