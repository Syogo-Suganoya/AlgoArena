INF = 10**15  # 無限大の値（経路が存在しない場合に使用）

# N: 頂点数、M: 辺の数
N, M = map(int, input().split())

# dist[i][j]: 頂点 i から頂点 j までの最短距離
dist = [[INF] * (N + 1) for _ in range(N + 1)]

# 辺の情報を読み込む
for _ in range(M):
    a, b, c = map(int, input().split())
    # 同じ辺が複数ある場合は最小のコストを採用
    if dist[a][b] > c:
        dist[a][b] = dist[b][a] = c

# 特別な頂点 0 の処理
K, T = map(int, input().split())  # K: 特別な頂点数, T: その距離
D = list(map(int, input().split()))  # 特別な頂点のリスト

# 頂点 0 と特別な頂点の距離を設定
for x in D:
    dist[x][0] = T  # 特別な頂点から 0 までの距離
    dist[0][x] = 0  # 0 から特別な頂点までの距離

# 自分自身への距離は 0
for i in range(N + 1):
    dist[i][i] = 0

# ワーシャルフロイド法で全点間最短距離を計算
for k in range(N + 1):
    dk = dist[k]
    for i in range(N + 1):
        di = dist[i]
        for j in range(N + 1):
            if di[k] + dk[j] < di[j]:
                di[j] = di[k] + dk[j]

# クエリ処理
for _ in range(int(input())):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # クエリ1: 辺の更新
        x, y, t = query[1:]
        if t >= dist[x][y]:  # 既存の距離の方が小さければスキップ
            continue
        dist[x][y] = dist[y][x] = t  # 辺の距離を更新

        # 更新後の最短距離を再計算
        for i in range(N + 1):
            di = dist[i]
            dx = dist[x]
            dy = dist[y]
            for j in range(N + 1):
                # x 経由、y 経由の最短距離を比較
                if di[x] + t + dy[j] < di[j]:
                    di[j] = di[x] + t + dy[j]
                if di[y] + t + dx[j] < di[j]:
                    di[j] = di[y] + t + dx[j]

    elif query[0] == 2:
        # クエリ2: 特別頂点 0 との距離更新
        x = query[1]
        if dist[x][0] == T:  # 既に T なら何もしない
            continue
        dist[x][0] = T
        dist[0][x] = 0

        # 更新後の最短距離を再計算
        for i in range(N + 1):
            di = dist[i]
            dx = dist[x]
            d0 = dist[0]
            for j in range(N + 1):
                if di[x] + T + d0[j] < di[j]:
                    di[j] = di[x] + T + d0[j]
                if di[0] + dx[j] < di[j]:
                    di[j] = di[0] + dx[j]

    elif query[0] == 3:
        # クエリ3: 全点間距離の合計
        total = 0
        for i in range(1, N + 1):
            di = dist[i]
            for j in range(1, N + 1):
                if di[j] < INF:
                    total += di[j]
        print(total)
