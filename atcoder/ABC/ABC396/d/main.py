N, M = map(int, input().split())
G = [[] for _ in range(N)]  # 隣接リスト (頂点番号は0-indexed)

# グラフ構築
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1  # 0-indexedに直す
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))  # 無向グラフ

ans = float("inf")  # XORの最小値を管理する

visited = [False] * N  # 訪問管理


def dfs(v, xor_sum):
    """
    頂点 v から頂点 N-1 までの経路をDFSで探索。
    xor_sumは、これまでに通った辺のラベルのXORの和。

    目的地に着いたら、グローバル変数 ans を更新する。
    """
    global ans
    visited[v] = True

    if v == N - 1:
        # 目的地に到達。XORの最小値を更新
        ans = min(ans, xor_sum)

    for u, w in G[v]:
        if not visited[u]:
            dfs(u, xor_sum ^ w)  # 次の頂点へ。ラベルwをXORで更新
    visited[v] = False  # 戻るときは訪問解除


dfs(0, 0)
print(ans)
