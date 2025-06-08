N, M = map(int, input().split())

# グラフの隣接リスト表現
graph = [[] for _ in range(N)]

# 辺情報を読み取り、グラフを構築（無向グラフ）
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1  # 0-indexed に変換
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

# 閉路の個数を求めるには、「各連結成分について 閉路 = 辺数 - 頂点数 + 1」
visited = [False] * N
cycle_count = 0


def dfs(v):
    stack = [v]
    node_count = 0
    edge_count = 0
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        node_count += 1
        for neighbor in graph[u]:
            edge_count += 1
            if not visited[neighbor]:
                stack.append(neighbor)
    return (node_count, edge_count // 2)  # 無向グラフなので辺は2回カウントされる


# 各連結成分ごとに探索
for i in range(N):
    if not visited[i]:
        nodes, edges = dfs(i)
        cycle_count += edges - nodes + 1

print(cycle_count)
