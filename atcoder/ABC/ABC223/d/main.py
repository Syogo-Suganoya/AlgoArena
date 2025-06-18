import heapq

N, M = map(int, input().split())

# グラフの隣接リストを作る（有向グラフ）
G = [[] for _ in range(N + 1)]

# 入次数（その頂点に向かって何本の辺があるか）
indegree = [0] * (N + 1)

# 制約を読み込み：A → B（AはBより先に来る）
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    indegree[B] += 1  # Bに入ってくる矢印が1本増える

# 優先度付きキュー（ヒープ）で、辞書順最小を実現
hq = []

# 最初に入次数が0の頂点をキューに入れる
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)

# 答えを格納するリスト
ans = []

while hq:
    u = heapq.heappop(hq)  # 辞書順で最小の頂点を取り出す
    ans.append(u)

    # uから出る矢印を辿って、行き先の入次数を減らす
    for v in G[u]:
        indegree[v] -= 1
        # 入次数が0になったらキューに追加（次に使えるように）
        if indegree[v] == 0:
            heapq.heappush(hq, v)

# 答えの長さがNなら正しい順列、それ以外は矛盾あり（-1を出力）
if len(ans) == N:
    print(*ans)
else:
    print(-1)
