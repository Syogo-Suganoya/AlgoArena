from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

color = [-1] * N
is_bipartite = True

for start in range(N):
    if color[start] != -1:
        continue
    queue = deque([start])
    color[start] = 0

    while queue and is_bipartite:
        v = queue.popleft()
        for nei in graph[v]:
            if color[nei] == -1:
                color[nei] = color[v] ^ 1
                queue.append(nei)
            elif color[nei] == color[v]:
                is_bipartite = False
                break

print("Yes" if is_bipartite else "No")
