class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root  # y_root を x_root にくっつける


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1  # 0-indexed にする
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

dsu = DSU(N)

for u in range(N):
    for v in graph[u]:
        dsu.unite(u, v)

# 連結成分数を数える
roots = set()
for i in range(N):
    roots.add(dsu.find(i))

print(len(roots))
