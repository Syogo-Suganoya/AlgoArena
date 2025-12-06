import sys

sys.setrecursionlimit(10**7)

n = int(input())
graph = [[] for _ in range(n)]
edges = []

# 辺情報を保持しつつグラフ構築
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, i))
    graph[b].append((a, i))
    edges.append((a, b))

# 最大次数が必要な色数 K
K = max(len(g) for g in graph)
print(K)

colors = [-1] * (n - 1)  # 各辺の色を保存
visited = [False] * n


def dfs(v, parent_color):
    visited[v] = True
    color = 1  # 今の頂点で使う色候補

    for nv, idx in graph[v]:
        if visited[nv]:
            continue

        if color == parent_color:
            color += 1  # 親から来た色はスキップ

        colors[idx] = color
        dfs(nv, color)
        color += 1


# 根を 0 として DFS
dfs(0, 0)

# 辺の順番で出力
print("\n".join(map(str, colors)))
