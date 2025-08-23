from heapq import heappop, heappush


# ダイクストラ法を使って「startからの最短距離」を求める関数
# 戻り値は「最も遠い頂点の番号」と「その距離」
def dijk(start):
    dist = [INF] * N  # 各頂点への最短距離を INF で初期化
    dist[start] = 0  # 自分自身への距離は0
    hq = []
    heappush(hq, (0, start))  # (距離, 頂点) のタプルを優先度付きキューに入れる

    while hq:
        d, v = heappop(hq)  # 距離が最小の頂点を取り出す

        if dist[v] != d:  # 既により良い距離が確定しているならスキップ
            continue

        # 隣接頂点を探索
        for nxt, c in G[v]:
            nc = d + c  # vを経由したときの距離
            if dist[nxt] > nc:  # より短ければ更新
                dist[nxt] = nc
                heappush(hq, (nc, nxt))

    # もっとも遠い頂点とその距離を返す
    mx = max(dist)
    idx = dist.index(mx)
    return (idx, mx)


N = int(input())
ABC = [list(map(int, input().split())) for i in range(N - 1)]
INF = 10**18
G = [[] for i in range(N)]
ans = 0

# グラフ（木）を構築
for a, b, c in ABC:
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))
    ans += 2 * c  # 各辺を往復するので「×2」を足す

# まずは0から最も遠い頂点を探す
i1, _ = dijk(0)

# さらにその頂点から最も遠い頂点を探す
# これで求められる距離が「木の直径」
i2, mx2 = dijk(i1)

# 答え = 全往復 - 木の直径
# 最後の人が「戻ってこなくていい」ぶんを引く
print(ans - mx2)
