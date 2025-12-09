import sys

sys.setrecursionlimit(10**7)
N, M = map(int, input().split())

# 隣接リスト（Z_i は使わない！繋がっていれば良いため）
G = [[] for _ in range(N)]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    X -= 1
    Y -= 1
    # 条件により X と Y が同じ成分に属する
    G[X].append(Y)
    G[Y].append(X)

visited = [False] * N


# DFS で連結成分の数を数える
def dfs(s):
    stack = [s]
    visited[s] = True
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if not visited[nv]:
                visited[nv] = True
                stack.append(nv)


comp = 0
for i in range(N):
    if not visited[i]:
        comp += 1
        dfs(i)

print(comp)
