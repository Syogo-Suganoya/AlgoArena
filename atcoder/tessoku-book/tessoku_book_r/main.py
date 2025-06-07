N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[x] = True なら、和が x になるような選び方が存在する
dp = [False] * (S + 1)
dp[0] = True  # 何も選ばなければ和は0

# 各数字を使って更新していく
for a in A:
    for x in range(S, a - 1, -1):  # 大きい方からループ（aを1回しか使わないため）
        if dp[x - a]:
            dp[x] = True

# 結果の出力
print("Yes" if dp[S] else "No")
