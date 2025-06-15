N, M = map(int, input().split())
E = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    E[a][b] = c
    E[b][a] = c

ans = 0
used = [False] * (N + 1)


def dfs(v, s):
    """
    深さ優先探索で頂点vからスタートし、現在の合計重みsを引き継ぐ。
    """
    global ans
    used[v] = True  # 頂点vを訪問済みにする

    # 現時点の合計重みsがこれまでの最大値ansを超えれば更新
    if s > ans:
        ans = s

    # 頂点vから行けるすべての隣接頂点を探索
    for i in range(1, N + 1):
        # まだ訪れていない頂点で、かつ辺が存在する場合
        if not used[i] and E[v][i]:
            dfs(i, s + E[v][i])  # 辺の重みを加えて再帰的に探索

    used[v] = (
        False  # vの探索が終わったら訪問済みフラグを戻す（他ルートでの再利用のため）
    )


# グラフの全頂点を起点として深さ優先探索を実行
for i in range(1, N + 1):
    dfs(i, 0)

# 探索終了後、最大の重み和を出力
print(ans)
