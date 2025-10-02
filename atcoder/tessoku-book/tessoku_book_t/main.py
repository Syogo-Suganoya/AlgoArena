def lcs(s, t):
    len_s, len_t = len(s), len(t)
    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 最長共通部分列の復元
    lcs_str = []
    i, j = len_s, len_t
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            lcs_str.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_str))


# 入力例
s = input()
t = input()

# 実行
print(len(lcs(s, t)))
