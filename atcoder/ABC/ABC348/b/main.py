N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 各点から最も遠い点のインデックスを格納するリスト
res = [-1] * N

# 各点 i についてループ
for i in range(N):
    max_dist = -1  # i からの最大距離を記録
    for j in range(N):
        if i == j:
            continue  # 自分自身との距離はスキップ

        # 2点間の距離を計算（ユークリッド距離）
        xi, yi = points[i]
        xj, yj = points[j]
        dist = (xi - xj) ** 2 + (yi - yj) ** 2  # 距離の二乗で比較すれば十分

        # 最大距離を更新
        if dist > max_dist:
            max_dist = dist
            res[i] = j + 1  # 1-indexed で格納

# 結果を出力
print(*res)
