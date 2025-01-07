# Union-Findの実装
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


# 入力
H, W = map(int, input().split())
Q = int(input())


# 1次元で座標を管理
def to_id(r, c):
    return r * W + c


# 初期化
uf = UnionFind(H * W)
red = [[False] * W for _ in range(H)]  # 各マスが赤かどうかを管理

# 移動方向
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# クエリ処理
for _ in range(Q):
    query = input().split()
    if query[0] == "1":  # 塗りつぶしクエリ
        r, c = int(query[1]) - 1, int(query[2]) - 1
        red[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and red[nr][nc]:
                uf.union(to_id(r, c), to_id(nr, nc))
    elif query[0] == "2":  # 連結性判定クエリ
        r1, c1 = int(query[1]) - 1, int(query[2]) - 1
        r2, c2 = int(query[3]) - 1, int(query[4]) - 1
        if red[r1][c1] and red[r2][c2] and uf.same(to_id(r1, c1), to_id(r2, c2)):
            print("Yes")
        else:
            print("No")
