from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフの隣接リスト（0-indexed）

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)

ans = 0

# 各都市をスタートにして探索
for s in range(N):
    vis = [False] * N
    vis[s] = True
    queue = deque([s])
    reached = 1  # スタート地点自身も到達可

    while queue:
        u = queue.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v] = True
                queue.append(v)
                reached += 1

    ans += reached

print(ans)
