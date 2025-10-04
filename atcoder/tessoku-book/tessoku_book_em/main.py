class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)


# 入力
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u - 1, v - 1))  # 0-index に直す

Q = int(input())
queries = []
removed = [False] * M  # 各辺が運休されたかどうか

for _ in range(Q):
    q = input().split()
    if q[0] == "1":  # 運休
        x = int(q[1]) - 1  # 路線番号を0-indexに
        queries.append(("1", x))
        removed[x] = True
    else:
        u, v = int(q[1]) - 1, int(q[2]) - 1
        queries.append(("2", u, v))

# 逆順に処理する
uf = UnionFind(N)

# 初期状態：運休にならない辺を追加
for i in range(M):
    if not removed[i]:
        u, v = edges[i]
        uf.unite(u, v)

answers = []

# 逆順でクエリを処理
for q in reversed(queries):
    if q[0] == "1":  # 本来は削除だが、逆順なので追加
        x = q[1]
        u, v = edges[x]
        uf.unite(u, v)
    else:  # q[0] == "2"
        u, v = q[1], q[2]
        if uf.same(u, v):
            answers.append("Yes")
        else:
            answers.append("No")

# 最後に順番を戻して出力
for ans in reversed(answers):
    print(ans)
