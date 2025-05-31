from collections import deque

N1, N2, M = map(int, input().split())
graph = [[] for _ in range(N1 + N2 + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    dist = [-1] * (N1 + N2 + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist


# 1からの最短距離
dist1 = bfs(1)
# N1+N2からの最短距離
dist2 = bfs(N1 + N2)

# 1〜N1の中で最も遠い頂点までの距離
max1 = max(dist1[1 : N1 + 1])
# N1+1〜N1+N2の中で最も遠い頂点までの距離
max2 = max(dist2[N1 + 1 :])

# それらの和に+1して出力
print(max1 + max2 + 1)
