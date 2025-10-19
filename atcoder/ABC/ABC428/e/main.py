# 非再帰DFS：スタックを使って深さを計算
def dfs_stack(start, dist, g):
    stack = [(start, 0)]  # (ノード, 深さ)
    dist[start] = 0
    while stack:
        c, depth = stack.pop()
        for d in g[c]:
            if dist[d] != -1:
                continue
            dist[d] = depth + 1
            stack.append((d, depth + 1))


N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

# 1回目：頂点0から最も遠い点uを探す
d0 = [-1] * N
dfs_stack(0, d0, g)
u = max([(d0[i], i) for i in range(N)])[1]

# 2回目：uから最も遠い点vを探す
du = [-1] * N
dfs_stack(u, du, g)
v = max([(du[i], i) for i in range(N)])[1]

# 3回目：vからの距離を計算
dv = [-1] * N
dfs_stack(v, dv, g)

# 各頂点iについて、より遠い方（u側 or v側）の端点を出力
for i in range(N):
    print(max((du[i], u), (dv[i], v))[1] + 1)
