import heapq

N, M = map(int, input().split())

# G: 順方向グラフ
# rG: 逆方向グラフ（戻るための辺を探す用）
G = [[] for _ in range(N)]
rG = [[] for _ in range(N)]

# 辺の入力
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1  # 0-indexed に変換
    B -= 1
    G[A].append((B, C))  # A → B（コスト C）
    rG[B].append((A, C))  # 逆向きの辺（B → A）

# ------------------------------
# 各頂点 i について、
# 「i から出発して i に戻る最短閉路」を求める
# ------------------------------
for i in range(N):
    # dist[v]: 頂点 i から v までの最短距離
    INF = 10**10
    dist = [INF] * N
    dist[i] = 0

    # Dijkstra 法（最小ヒープ使用）
    queue = []
    heapq.heappush(queue, (0, i))  # (距離, 頂点)

    while queue:
        c, v = heapq.heappop(queue)
        # すでにより短い経路があるならスキップ
        if dist[v] < c:
            continue
        # 隣接頂点を探索
        for nxt, d in G[v]:
            # より短い経路を発見したら更新
            if dist[nxt] > c + d:
                dist[nxt] = c + d
                heapq.heappush(queue, (c + d, nxt))

    # ------------------------------
    # 頂点 i に戻る閉路の最短長を探す
    # ------------------------------
    ans = INF
    # rG[i] には「i へ戻る辺 (j → i, cost)」が入っている
    for j, d in rG[i]:
        # i → ... → j → i の経路長 = dist[j] + d
        ans = min(ans, dist[j] + d)

    # 閉路が存在すれば最短距離を、なければ -1 を出力
    print(ans if ans != INF else -1)
