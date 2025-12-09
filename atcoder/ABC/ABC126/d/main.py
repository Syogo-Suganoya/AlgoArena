import sys

# 再帰の上限を引き上げ（N が大きくても DFS が落ちないようにする）
sys.setrecursionlimit(10**7)

N = int(input())

# 隣接リスト（各頂点に「行き先・重み」のペアを持たせる）
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1  # 0-index 化
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

# 各頂点の色（0 or 1）。未訪問は -1
colors = [-1] * N


def dfs(u, parent, col):
    """
    u: 現在いる頂点
    parent: 親頂点（逆流しないようにするため）
    col: 現在の頂点に塗る色（0 or 1）

    辺が偶数重なら同じ色、奇数重なら色を反転する。
    """
    colors[u] = col  # 頂点 u の色を確定

    # 隣接する頂点をすべて探索
    for v, w in adj[u]:
        if v == parent:
            continue  # 親に戻らない

        # w が偶数：色は変えない
        if w % 2 == 0:
            dfs(v, u, col)
        # w が奇数：色を反転する
        else:
            dfs(v, u, 1 - col)


# 根（0番目の頂点）を色0で塗って DFS 開始
dfs(0, -1, 0)

for c in colors:
    print(c)
