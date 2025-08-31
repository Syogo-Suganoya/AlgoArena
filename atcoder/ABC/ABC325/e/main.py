import heapq  # 優先度付きキュー（ヒープ）を使うためにインポート

INF = float("inf")  # 無限大を表す値

# 入力: 都市数 N、社用車コスト A、電車コスト B、電車乗車固定費 C
N, A, B, C = map(int, input().split())

# 各都市間の距離行列 D[u][v] を入力
D = [list(map(int, input().split())) for _ in range(N)]

# dp[i][0]: 都市 i に社用車で到達する最短時間
# dp[i][1]: 都市 i に電車で到達する最短時間
dp = [[INF, INF] for _ in range(N)]
dp[0][0] = 0  # 初期都市 0 に社用車で到達する時間は0
# 電車での初期到達は不可能なので INF のまま

# 優先度付きキューに初期状態を投入
# (時間, 都市, 移動手段)
pq = [(0, 0, 0), (0, 0, 1)]

while pq:
    t, u, mode = heapq.heappop(pq)  # 時間 t で都市 u に mode で到達

    # 既により良い到達時間が記録されていればスキップ
    if dp[u][mode] < t:
        continue

    # 都市 u から他の都市 v への遷移をすべて確認
    for v in range(N):
        if mode == 0:  # 現在社用車の場合
            # 1. 社用車で移動
            new_time = t + D[u][v] * A
            if dp[v][0] > new_time:
                dp[v][0] = new_time
                heapq.heappush(pq, (new_time, v, 0))  # キューに追加

            # 2. 社用車 → 電車に乗り換える
            new_time = t + D[u][v] * B + C
            if dp[v][1] > new_time:
                dp[v][1] = new_time
                heapq.heappush(pq, (new_time, v, 1))  # キューに追加

        else:  # 現在電車の場合
            # 電車での移動しかできない（社用車には戻れない）
            new_time = t + D[u][v] * B + C
            if dp[v][1] > new_time:
                dp[v][1] = new_time
                heapq.heappush(pq, (new_time, v, 1))  # キューに追加

# 最終都市 N-1 に到達する最短時間は社用車・電車の両方の最小値
print(min(dp[N - 1][0], dp[N - 1][1]))
