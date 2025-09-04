import sys

sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))  # 0-index化

visited = [0] * N  # 0=未訪問, 1=探索中, 2=確定
in_cycle = [False] * N


def dfs(v):
    path = []
    while True:
        if visited[v] == 1:
            # サイクル検出
            idx = path.index(v)
            for u in path[idx:]:
                in_cycle[u] = True
            break
        if visited[v] == 2:
            break
        visited[v] = 1
        path.append(v)
        v = A[v]
    for u in path:
        visited[u] = 2


for i in range(N):
    if visited[i] == 0:
        dfs(i)

# サイクルに含まれる頂点の数が答え
print(sum(in_cycle))
