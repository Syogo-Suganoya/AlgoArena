s = input().strip()
n = len(s)

# 十分小さい値（不可能な状態の表現）
NEG_INF = -(10**9)

# f[l][r] : 区間 s[l..r] を完全に消せるときの最大取り除き回数，消せないなら NEG_INF
f = [[NEG_INF] * n for _ in range(n)]

# 長さ0の区間は「何もない」として 0 回とみなす（後の考えのため）
# ここでは f[l][r] は l<=r の区間のみ扱う．

# 長さ1以上の区間について，区間の長さ順に計算
for length in range(1, n + 1):
    for l in range(0, n - length + 1):
        r = l + length - 1
        # まずは分割による消去：どこかで区間を分ける
        for m in range(l, r):
            if f[l][m] != NEG_INF and f[m + 1][r] != NEG_INF:
                f[l][r] = max(f[l][r], f[l][m] + f[m + 1][r])
        # 次に直接 "iwi" で削除できる形かを確認
        if length >= 3 and s[l] == "i" and s[r] == "i":
            # 中間で 'w' となる文字の位置 m を探す
            for m in range(l + 1, r):
                if s[m] == "w":
                    left_val = 0
                    right_val = 0
                    # s[l+1...m-1] が空なら0，それ以外なら f[l+1][m-1] の値
                    if m - l - 1 > 0:
                        left_val = f[l + 1][m - 1]
                    # s[m+1...r-1] が空なら0
                    if r - m - 1 > 0:
                        right_val = f[m + 1][r - 1]
                    if left_val != NEG_INF and right_val != NEG_INF:
                        f[l][r] = max(f[l][r], left_val + right_val + 1)
        # さらに，"完全に消せる" とは言えなくても，長さが3であれば直接 "iwi" のときは削除可能
        if length == 3 and s[l : l + 3] == "iwi":
            f[l][r] = max(f[l][r], 1)

# dp[i] : s[0...i-1]までで，非重複に取り除ける回数の最大値
dp = [-(10**9)] * (n + 1)
dp[0] = 0
for i in range(n):
    # iから j までが完全に消せるなら，
    for j in range(i, n):
        if f[i][j] != NEG_INF:
            dp[j + 1] = max(dp[j + 1], dp[i] + f[i][j])
    # また，何も取り除かずに1文字進める場合（その文字を残す）も考える
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])
