import itertools

# 入力の読み込み
N = int(input())
M_G = int(input())
G = [[False] * N for _ in range(N)]
for _ in range(M_G):
    u, v = map(int, input().split())
    G[u - 1][v - 1] = True
    G[v - 1][u - 1] = True

M_H = int(input())
H = [[False] * N for _ in range(N)]
for _ in range(M_H):
    a, b = map(int, input().split())
    H[a - 1][b - 1] = True
    H[b - 1][a - 1] = True

A = [[0] * N for _ in range(N)]
for i in range(N - 1):
    row = list(map(int, input().split()))
    for j in range(i + 1, N):
        A[i][j] = row[j - i - 1]
        A[j][i] = A[i][j]  # 対称性を利用

# 最小コストの初期化
min_cost = float("inf")

# 全ての頂点の順列を試す
for perm in itertools.permutations(range(N)):
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            # 順列に基づいてグラフ G の辺を確認
            g_edge = G[perm[i]][perm[j]]
            h_edge = H[i][j]
            if g_edge != h_edge:
                cost += A[i][j]
    min_cost = min(min_cost, cost)

print(min_cost)
