N, M = map(int, input().split())

# 隣接リスト G を用意 (0-indexed)
#   G[u] = [(v, w)]  … 辺  u → v  の重み w (x_v - x_u = w)
# 逆方向を重み -w で入れておくことで
#   u → v の制約  x_v = x_u + w
#   v → u の制約  x_u = x_v - w
# が同時に扱えるようになる（双方向化）
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1  # 0-index へ
    v -= 1
    G[u].append((v, w))  # 順方向
    G[v].append((u, -w))  # 逆方向（重みは -w）

# --- DFS/BFS 用の配列 ---
visited = [False] * N  # その頂点の値が既に確定したか
ans = [0] * N  # 各頂点の値 x_i を格納する

# --- 連結成分ごとに探索 ---
for i in range(N):
    if visited[i]:
        continue  # すでに確定済みならスキップ

    # 連結成分の基準点として頂点 i の値を 0 に決め打ち
    # （0 でなくても良いが、任意の基準を置くだけ）
    stack = [i]
    visited[i] = True
    ans[i] = 0

    # 深さ優先で値を伝播していく
    while stack:
        u = stack.pop()  # 現在の頂点

        # 隣接する頂点 v へ
        for v, w in G[u]:
            if not visited[v]:
                # 制約式      x_v - x_u =  w
                # → 求めたい x_v = x_u + w
                ans[v] = ans[u] + w
                visited[v] = True
                stack.append(v)
                # これで v の値が確定し、次に v からも伝播する

print(*ans)
