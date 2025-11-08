N, M, L = map(int, input().split())
A = list(map(int, input().split()))

# --- 1️⃣ 各グループ（インデックス mod L）ごとに分ける ---
groups = [[] for _ in range(L)]
for i in range(N):
    groups[i % L].append(A[i])

# --- 2️⃣ 各グループを値の剰余 j に揃えるためのコストを計算 ---
# cost[i][j] = i番目のグループを全て値 j にするのに必要な「+1操作」回数
cost = [[0] * M for _ in range(L)]

for i in range(L):
    for j in range(M):
        total = 0
        for a in groups[i]:
            # (j - a + M) % M は a を j に合わせるために必要な操作回数
            total += (j - a) % M
        cost[i][j] = total

# --- 3️⃣ DPテーブル初期化 ---
# dp[i][r] = グループ0〜i-1を決めた状態で、現在の剰余の合計がrになる最小コスト
INF = 10**18
dp = [[INF] * M for _ in range(L + 1)]
dp[0][0] = 0

# --- 4️⃣ DP 遷移 ---
for i in range(L):
    for r in range(M):  # 現在の剰余合計
        if dp[i][r] == INF:
            continue
        for j in range(M):  # i番目のグループを j に揃える
            nr = (r + j) % M
            dp[i + 1][nr] = min(dp[i + 1][nr], dp[i][r] + cost[i][j])

# --- 5️⃣ 答え出力 ---
# 最終的に合計剰余が0（＝全ての長さL部分列の和がMの倍数）
ans = dp[L][0]
print(ans)
