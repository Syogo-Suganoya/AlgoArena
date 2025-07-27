from collections import deque

MOD = 10**9 + 7  # 答えを出力する際のMOD

N, M = map(int, input().split())  # 頂点数N、辺数Mの読み込み

# グラフの隣接リスト表現（1-indexed）
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# dist[i] = 頂点1から頂点iまでの最短距離（-1は未訪問）
dist = [-1] * (N + 1)

# cnt[i] = 頂点1から頂点iまでの最短経路の数
cnt = [0] * (N + 1)

# 頂点1の初期化
dist[1] = 0
cnt[1] = 1

# BFSのためのキュー
q = deque([1])

# 幅優先探索開始
while q:
    u = q.popleft()  # 現在の頂点

    for v in G[u]:  # 隣接する頂点をチェック
        if dist[v] == -1:
            # 初めて訪れた頂点 → 最短距離確定
            dist[v] = dist[u] + 1
            cnt[v] = cnt[u]  # 経路数はそのまま引き継ぐ
            q.append(v)
        elif dist[v] == dist[u] + 1:
            # すでに最短距離で訪れている → 経路数を加算
            cnt[v] = (cnt[v] + cnt[u]) % MOD

# 頂点Nまでの最短経路の数を出力
print(cnt[N])
