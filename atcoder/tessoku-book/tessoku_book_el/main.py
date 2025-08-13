import sys

sys.setrecursionlimit(10**7)

N, T = map(int, input().split())
T -= 1  # 0-index に調整

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

rank = [0] * N


def dfs(v, p):
    max_sub = 0
    for u in graph[v]:
        if u == p:
            continue
        child_rank = dfs(u, v)
        max_sub = max(max_sub, child_rank)
    rank[v] = max_sub
    return max_sub + 1


dfs(T, -1)

# 0-index から番号順に整えて出力
print(*rank)
