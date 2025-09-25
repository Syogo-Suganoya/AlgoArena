MOD = 10**9 + 7

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1  # 0-indexed に
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

# dp[i][0]: 頂点 i を選ばない場合の独立集合の数
# dp[i][1]: 頂点 i を選ぶ場合の独立集合の数
dp = [[1, 1] for _ in range(N)]

# 親を管理して再帰を使わない DFS を実現
parent = [-1] * N
stack = [0]  # 根を 0 とする
order = []  # DFS の訪問順序を記録

# --- 非再帰 DFS ---
while stack:
    u = stack.pop()
    order.append(u)  # 訪問順を保存
    for v in edges[u]:
        if v == parent[u]:
            continue
        parent[v] = u  # 親を記録
        stack.append(v)

# --- DP 計算（葉から根へ逆順に計算） ---
for u in reversed(order):
    for v in edges[u]:
        if v == parent[u]:
            continue
        # u を選ばない場合は子を選ぶ/選ばない 両方 OK
        dp[u][0] = dp[u][0] * (dp[v][0] + dp[v][1]) % MOD
        # u を選ぶ場合は子は選べない
        dp[u][1] = dp[u][1] * dp[v][0] % MOD

# 根を選ぶ場合と選ばない場合の合計が答え
print((dp[0][0] + dp[0][1]) % MOD)
