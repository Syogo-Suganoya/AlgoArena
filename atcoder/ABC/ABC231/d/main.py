class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n  # 負の値は根であり、絶対値は集合のサイズ

    def find(self, x):
        if self.parent[x] < 0:
            return x
        # 経路圧縮
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False  # すでに同じ集合に属する
        # サイズの大きい方に統合
        if self.parent[x_root] > self.parent[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[x_root] += self.parent[y_root]
        self.parent[y_root] = x_root
        return True


N, M = map(int, input().split())


def main():
    uf = UnionFind(N)
    degree = [0] * N  # 各頂点の次数を管理

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1  # 0-indexed に変換
        b -= 1
        degree[a] += 1
        degree[b] += 1
        if degree[a] > 2 or degree[b] > 2:
            return False
        if not uf.unite(a, b):
            return False
    return True


print("Yes" if main() else "No")
