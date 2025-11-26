N = int(input())
XYP = [list(map(int, input().split())) for _ in range(N)]

# dist[i][j] : ジャンプ台 i から j へ直接行くために必要な S の最小値
# 到達不能（自分自身など）は便宜上 0 とする
dist = [[0] * N for _ in range(N)]

for i in range(N):
    xi, yi, pi = XYP[i]
    for j in range(N):
        if i == j:
            continue
        xj, yj, pj = XYP[j]

        # マンハッタン距離
        d = abs(xi - xj) + abs(yi - yj)

        # 必要なSは ceil(d / pi)
        # 整数演算で切り上げ: (d + pi - 1) // pi
        dist[i][j] = (d + pi - 1) // pi

# ワーシャル・フロイド法 (Min-Max Path)
# i -> j へ行く経路の中で、最大の S が最小になるような経路を探す
for k in range(N):
    for i in range(N):
        for j in range(N):
            # i -> k -> j と経由する場合のコスト
            # 経路上の最大値をとる必要があるため max
            new_cost = max(dist[i][k], dist[k][j])

            # そのコストが今の i -> j よりも小さければ更新
            if new_cost < dist[i][j]:
                dist[i][j] = new_cost

# 答えを求める
# 各始点 i について、「全ての j に到達するために必要な S (行の最大値)」を求める
# その中で最小のものが答え
ans = float("inf")

for i in range(N):
    max_s_for_start_i = 0
    for j in range(N):
        max_s_for_start_i = max(max_s_for_start_i, dist[i][j])
    ans = min(ans, max_s_for_start_i)

print(ans)
