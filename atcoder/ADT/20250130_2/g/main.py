from collections import deque

N1, N2, M = map(int, input().split())

N = N1 + N2

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 無向グラフの場合


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
    # 各ノードの最短距離を返す
    return distances


distances = bfs(graph, 1)
dis_max = max(distances)  # 最大距離

distances2 = bfs(graph, N)
dis_max2 = max(distances2)  # 最大距離

print(dis_max + dis_max2 + 1)
