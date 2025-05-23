N = int(input())
A = list(map(int, input().split()))

# dp[k][s] := k枚選んで合計がsになる組み合わせの数
dp = [[0] * 1001 for _ in range(6)]  # 0〜5枚の各合計値を管理するDP表

dp[0][0] = 1  # 初期状態：0枚で合計0は1通り

# 各カードを順に処理
for a in A:
    # 後ろから更新することで、同じカードを複数回使うのを防ぐ（重複選びを防ぐ）
    for k in range(4, -1, -1):  # 5枚目→1枚目の順に逆から処理
        for s in range(1000 - a + 1):  # 合計値が1000を超えない範囲で遷移
            dp[k + 1][s + a] += dp[k][s]  # aを加えて1枚多く選んだ場合の合計を更新

print(dp[5][1000])
