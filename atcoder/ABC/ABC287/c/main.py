import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# 条件①：辺の数が N-1？
if M != N - 1:
    print("No")
    exit()

# 条件②：どの頂点も次数 ≤ 2？
for neighbors in graph:
    if len(neighbors) > 2:
        print("No")
        exit()

# DFS で連結チェック（条件③）
visited = [False] * N


def dfs(v):
    visited[v] = True
    for nx in graph[v]:
        if not visited[nx]:
            dfs(nx)


# 辺がある頂点からDFSスタート
start = next((i for i, nb in enumerate(graph) if nb), None)
if start is None:
    # 辺が1本もない → N>=2なら NG
    print("No")
    exit()

dfs(start)
# どの頂点も訪問されたか？
if all(visited[i] or not graph[i] for i in range(N)):
    print("Yes")
else:
    print("No")
