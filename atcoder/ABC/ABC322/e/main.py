from collections import defaultdict

# 入力
N, K, P = map(int, input().split())
plans = []
for _ in range(N):
    data = list(map(int, input().split()))
    C = data[0]  # 開発案のコスト
    A = data[1:]  # 開発案で上がるスキルのリスト（K 個）
    plans.append((C, A))

INF = float("inf")

# 各スキルが最低でも P 必要なので、目標の状態をタプルで持つ
goal = tuple([P] * K)

# dp[i][state] = 「i 個目までの開発案を考えたとき、スキル状態が state になる最小コスト」
# state は長さ K のタプルで、各スキル値を表す
# defaultdict を使って、初期値は INF にしている
dp = [defaultdict(lambda: INF) for _ in range(N + 1)]

# 初期状態（何も選んでいない状態）: スキルはすべて 0, コストは 0
dp[0][tuple([0] * K)] = 0

# 開発案を 1 つずつ見ていく
for i in range(N):
    C, A = plans[i]
    for state, cost in dp[i].items():
        # 1. 開発案 i を選ばない場合
        dp[i + 1][state] = min(dp[i + 1][state], cost)

        # 2. 開発案 i を選ぶ場合
        #    各スキルに A[j] を加える。ただし上限は P（超えても意味がない）
        new_state = tuple(min(state[j] + A[j], P) for j in range(K))
        dp[i + 1][new_state] = min(dp[i + 1][new_state], cost + C)

# 最後に「すべてのスキルが P 以上」の状態を達成できたか確認
print(dp[N][goal] if dp[N][goal] != INF else -1)
