from sortedcontainers import SortedList


# --- Union-Find (Disjoint Set Union) ---
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return x
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return x


N, Q = map(int, input().split())

dsu = DSU(N)
# 各成分ごとに SortedList を持つ（降順は後で index -k で対応する）
comp = {i: SortedList([i]) for i in range(N)}

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        # 辺を追加
        u, v = int(query[1]) - 1, int(query[2]) - 1
        ru, rv = dsu.find(u), dsu.find(v)
        if ru != rv:
            new_root = dsu.union(ru, rv)
            old_root = rv if new_root == ru else ru
            # small-to-large マージ
            if len(comp[new_root]) < len(comp[old_root]):
                comp[new_root], comp[old_root] = comp[old_root], comp[new_root]
            comp[new_root].update(comp[old_root])
            del comp[old_root]

    else:
        # k番目に大きい頂点を出力
        v, k = int(query[1]) - 1, int(query[2])
        r = dsu.find(v)
        arr = comp[r]
        if len(arr) >= k:
            print(arr[-k] + 1)  # -k で降順の k 番目、+1 で1-index化
        else:
            print(-1)
