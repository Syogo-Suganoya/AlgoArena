# 入力
N = int(input())
S = input().strip()

MOD = 10**9 + 7
target = "atcoder"

# DPテーブルの初期化
dp = [[0] * (len(target) + 1) for _ in range(len(S) + 1)]
dp[0][0] = 1  # 空文字列を使って空文字列を作る方法は1通り

# DP遷移
for i in range(1, len(S) + 1):
    dp[i] = dp[i - 1][:]  # 深いコピーで新しいリストを作成
    now_S = S[i - 1]
    if now_S in target:
        j = target.index(now_S) + 1
        dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

# 結果
print(dp[-1][-1])
