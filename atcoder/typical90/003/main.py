from collections import deque

N = int(input())


def bfs(graph, start):
    # グラフ内のノード数
    n = len(graph)
    # 各ノードの距離を格納するリスト（-1は未訪問を示す）
    distances = [-1] * n
    distances[start] = 0  # 開始ノードの距離を0に設定
    # 探索のためのデキュー（FIFOキュー）
    queue = deque([start])
    # BFSのメインループ
    while queue:
        # キューから先頭のノードを取り出し
        node = queue.popleft()
        # 現在のノードから到達可能な隣接ノードを探索
        for neighbor in graph[node]:
            # 未訪問ノードならば、距離を更新しキューに追加
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances


def longest_circular_road():
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: 任意の頂点(例えば1)から最遠の頂点を見つける
    distances1 = bfs(graph, 1)
    node_a = distances1.index(max(distances1))
    # Step 2: node_aから最遠の頂点を見つけ、その距離を求める
    distances2 = bfs(graph, node_a)
    diameter = max(distances2)
    # 最大スコアは直径 + 1
    return diameter + 1


print(longest_circular_road())
