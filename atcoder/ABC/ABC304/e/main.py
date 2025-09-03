def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def unite(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pb] = pa


N, M = map(int, input().split())
# Union-Find で連結成分を管理
parent = list(range(N + 1))
# 既存の M 本の辺で連結を作る
for _ in range(M):
    u, v = map(int, input().split())
    unite(u, v)

K = int(input())
# NG なペアの成分をセットで管理
NG = set()
for _ in range(K):
    x, y = map(int, input().split())
    a, b = sorted((find(x), find(y)))
    NG.add((a, b))

Q = int(input())
# クエリ
for _ in range(Q):
    p, q = map(int, input().split())
    a, b = sorted((find(p), find(q)))
    print("No" if (a, b) in NG else "Yes")
