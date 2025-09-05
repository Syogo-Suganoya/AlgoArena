import queue


# 組み合わせ C(N,2) を計算する関数
# N個の頂点から作れる辺の総数を求める
def com(N):
    return N * (N - 1) // 2


# 頂点の色を表す定数
WHITE, BLACK = 0, 1

# 入力
N, M = map(int, input().split())  # 頂点数 N, 辺の数 M
edges = [list(map(int, input().split())) for _ in range(M)]

# 隣接リストの作成
G = [[] for _ in range(N)]
for e in edges:
    u, v = e[0] - 1, e[1] - 1  # 0-index に変換
    G[u].append(v)
    G[v].append(u)

# 二部グラフ判定用の変数
num_ng_edges = 0  # 同色間の辺の総数
is_bipartite = True  # 二部グラフかどうか
color = [-1] * N  # -1=未塗り, 0=白, 1=黒

# 各連結成分を BFS で走査
for s in range(N):
    if color[s] != -1:
        continue  # すでに訪問済みならスキップ

    white_num, black_num = 0, 0  # 白色、黒色の頂点数をカウント

    # BFSのキューを初期化
    que = queue.Queue()
    que.put(s)
    color[s] = WHITE  # 開始点を白に塗る

    # BFSで連結成分を探索
    while not que.empty():
        v = que.get()

        # 色ごとの頂点数をカウント
        if color[v] == WHITE:
            white_num += 1
        else:
            black_num += 1

        # 隣接頂点をチェック
        for v2 in G[v]:
            if color[v2] != -1:
                # すでに塗られている場合、同じ色なら二部グラフでない
                if color[v2] == color[v]:
                    is_bipartite = False
            else:
                # 未塗りの頂点は反対色に塗ってキューに追加
                color[v2] = 1 - color[v]
                que.put(v2)

    # 同色間で作れる辺の数を累積
    num_ng_edges += com(white_num) + com(black_num)

# 最終答え
# 全頂点間の辺の総数から、既存の辺と同色間の辺を引く
# 二部グラフでなければ答えは 0
res = 0
if is_bipartite:
    res = com(N) - M - num_ng_edges
print(res)
