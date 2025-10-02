# 巡回セールスマン問題(TSP)
import math

# 入力
N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]

# 都市間距離を計算
cost = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        xi, yi = coords[i]
        xj, yj = coords[j]
        cost[i][j] = math.hypot(xi - xj, yi - yj)  # ユークリッド距離

# TSP DP（bit DP）
INF = float("inf")
dp = [[INF] * N for _ in range(1 << N)]
dp[1][0] = 0  # 0番都市からスタート

# mask: 訪れた都市の集合をビットで表現（0からN-1都市）
for mask in range(1 << N):  # 2^N通りの訪問集合をすべてチェック
    for u in range(N):  # 現在最後に訪れた都市 u を選ぶ
        if not (mask & (1 << u)):
            # u がまだ訪問していない集合 mask に含まれていなければスキップ
            continue
        for v in range(N):  # 次に移動する都市 v を選ぶ
            if mask & (1 << v):
                # v がすでに訪問済ならスキップ
                continue
            new_mask = mask | (1 << v)  # v を追加した新しい訪問集合を作る
            # dp[new_mask][v] を更新
            # dp[mask][u] + cost[u][v] は
            # 「現在の集合 mask で最後が u のときの距離 + u→v の距離」
            dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

# 最終的に全都市を回って0に戻る
ans = min(dp[(1 << N) - 1][v] + cost[v][0] for v in range(N))
print(ans)
