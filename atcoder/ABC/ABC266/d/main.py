N = int(input())
T = [0] * N
X = [0] * N
A = [0] * N

# 入力をそれぞれのリストに格納
for i in range(N):
    T[i], X[i], A[i] = map(int, input().split())

max_time = max(T) + 1  # 最大の時刻に対応するため +1

# dp[t][x]: 時刻tに座標xにいるときの最大の捕獲量
# 可能性のないところは -1 に初期化
dp = [[-1] * 5 for _ in range(max_time)]
dp[0][0] = 0  # 初期条件: 時刻0、座標0にいる

# 出現するすぬけ君を辞書に格納
snuke = dict()
for t, x, a in zip(T, X, A, strict=True):
    if t not in snuke:
        snuke[t] = dict()
    snuke[t][x] = a

# 各時刻ごとに更新していく
for t in range(1, max_time):
    for x in range(5):
        max_prev = -1
        # 1秒で移動できる範囲（x-1, x, x+1）を確認
        for dx in [-1, 0, 1]:
            nx = x + dx
            # 移動先の座標が有効で、そこに到達可能な場合のみ最大値を更新
            if 0 <= nx < 5 and dp[t - 1][nx] != -1:
                max_prev = max(max_prev, dp[t - 1][nx])
        if max_prev != -1:
            # 移動可能なら、その最大値をdpに記録
            dp[t][x] = max_prev
            # もし時刻tに座標xですぬけ君が出現するなら、捕獲量を加算
            if t in snuke and x in snuke[t]:
                dp[t][x] += snuke[t][x]

# 時刻max_time-1の全ての座標での最大値が答え
print(max(dp[-1]))
