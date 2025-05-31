import sys

sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))

# グラフの隣接リスト
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i].append(A[i - 1])

visited = [False] * (N + 1)
on_stack = [False] * (N + 1)
path = []
cycle = []


def dfs_cycle(v):
    visited[v] = True
    on_stack[v] = True
    path.append(v)  # 経路を記録

    for u in graph[v]:
        if not visited[u]:
            if dfs_cycle(u):
                return True
        elif on_stack[u]:
            # サイクルの始まりを見つけたので、
            # 経路からサイクル部分を抽出
            idx = path.index(u)
            global cycle
            cycle = path[idx:]  # サイクル部分だけ切り出し
            return True

    path.pop()  # 戻るときに取り除く
    on_stack[v] = False
    return False


# 頂点1からスタート
dfs_cycle(1)

# 出力
print(len(cycle))
print(*cycle)
