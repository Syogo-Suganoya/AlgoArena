from collections import deque

N, M = map(int, input().split())

# グラフ構築（隣接リスト）
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1  # 0-indexed に変換
    B -= 1
    G[A].append(B)
    G[B].append(A)

# BFSの準備
dist = [-1] * N  # 最短距離を保持（未訪問は -1）
dist[0] = 0
q = deque([0])

# 幅優先探索
while q:
    v = q.popleft()
    for nv in G[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            q.append(nv)

print(0)  # 頂点1（0-indexed で0）の距離は0
for i in range(1, N):
    print(dist[i])
