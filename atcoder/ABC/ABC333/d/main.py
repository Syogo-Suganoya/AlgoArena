# Union-Find（素集合データ構造）を使って部分木の管理をする
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 初期は各頂点が自分自身を親に持つ
        self.size = [1] * n  # 各グループのサイズは1で初期化

    def find(self, x):
        # 経路圧縮を使った find 関数
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def merge(self, x, y):
        # 2つの頂点をマージ（サイズが大きい方を親にする）
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]

    def groups(self):
        # 各ルートごとに所属メンバーを集める（グループを返す）
        root_members = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in root_members:
                root_members[root] = []
            root_members[root].append(i)
        return list(root_members.values())


def main():
    N = int(input())
    uf = UnionFind(N)

    # 辺を読み込んで、頂点1を除いた部分で Union-Find を構築
    for _ in range(N - 1):
        u, v = map(int, input().split())
        if u != 1:
            uf.merge(u - 1, v - 1)

    # グループの中で最大サイズのものを残す
    max_group_size = max(len(group) for group in uf.groups())

    # 残さなければならない最小人数 = 全体 - 最大グループ
    print(N - max_group_size)


if __name__ == "__main__":
    main()
