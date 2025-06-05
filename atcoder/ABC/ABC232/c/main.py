from itertools import permutations

# 入力の読み込み
n, m = map(int, input().split())

# グラフGの隣接行列の初期化
G = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = G[b - 1][a - 1] = 1

# グラフHの隣接行列の初期化
H = [[0] * n for _ in range(n)]
for _ in range(m):
    c, d = map(int, input().split())
    H[c - 1][d - 1] = H[d - 1][c - 1] = 1

# 全ての頂点の順列を試す
for p in permutations(range(n)):
    match = True
    for i in range(n):
        for j in range(n):
            if G[i][j] != H[p[i]][p[j]]:
                match = False
                break
        if not match:
            break
    if match:
        print("Yes")
        break
else:
    print("No")
