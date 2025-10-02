n = int(input())
s = input()

# dp[l][r] : 部分文字列 s[l..r] における最長回文部分列の長さ
# 初期値は 1（1文字は必ず回文）
dp = [[1] * n for _ in range(n)]

# 長さ2の区間に対して、同じ文字なら「2文字の回文」となる
for i in range(n - 1):
    if s[i] == s[i + 1]:
        dp[i][i + 1] = 2

# 区間の長さを伸ばしながら DP
for length in range(2, n):  # length=2 から n-1 まで
    for l in range(n - length):
        r = l + length  # 区間 [l, r] を考える

        # 片方を削って合わせる
        dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
        # 端が同じ場合：
        if s[l] == s[r]:
            # dp[l+1][r-1] に両端を加えて +2
            dp[l][r] = max(dp[l][r], dp[l + 1][r - 1] + 2)


# 答えは区間全体 [0, n-1] の最長回文部分列の長さ
print(dp[0][n - 1])
