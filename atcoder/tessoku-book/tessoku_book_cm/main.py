# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# DPテーブル: dp[i] = 合計が i になる部分集合が存在するか
dp = [False] * (K + 1)
dp[0] = True  # 何も選ばなくても合計0は作れる

# DP遷移
for a in A:
    for j in range(K, a - 1, -1):
        if dp[j - a]:
            dp[j] = True

# 結果を出力
print("Yes" if dp[K] else "No")
