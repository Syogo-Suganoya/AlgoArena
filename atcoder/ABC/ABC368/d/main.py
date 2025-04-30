from collections import deque

# N: 頂点数, K: 重要な頂点の数
N, K = map(int, input().split())

# グラフの隣接リストを初期化（各頂点に対する接続先の集合）
edge = [set() for _ in range(N)]

# グラフの辺を読み込む（無向グラフなので両方向に追加）
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1  # 0-indexed に調整
    b -= 1
    edge[a].add(b)
    edge[b].add(a)

# 重要なK個の頂点集合を読み込む（0-indexedにする）
V = set(map(int, input().split()))
V = set(x - 1 for x in V)

# 各頂点の次数（接続数）を計算
deg = [len(s) for s in edge]

# 現在の葉（次数1）をキューに追加
q = deque(i for i, d in enumerate(deg) if d == 1)

# 答えの初期値はN（すべて残す場合）
ans = N

# 葉から削除していく処理（逆BFSのようなもの）
while q:
    v = q.popleft()  # 現在の葉を取り出す

    # 重要な頂点は削除できない
    if v in V:
        continue

    # vの唯一の隣接頂点 vv を取得し、v を vv の隣接リストから削除
    vv = edge[v].pop()
    edge[vv].discard(v)

    # 1つ頂点を削除する
    ans -= 1

    # vv が新たに葉になった場合、次に処理する
    if len(edge[vv]) == 1:
        q.append(vv)

# 最終的に残った部分木の頂点数を出力
print(ans)
