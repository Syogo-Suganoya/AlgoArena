MOD = 10**9 + 7

K = input().strip()  # 上限の数 K（文字列で受け取る）
D = int(input().strip())  # 割る数 D

L = len(K)  # K の桁数

# dp[i][s][t] = i 桁目まで決めたときの方法数
# i: 何桁決めたか (0..L)
# s: 桁和の mod D の値 (0..D-1)
# t: フラグ 0 or 1
#    0 = 今まで K の接頭辞と一致している
#    1 = すでに K より小さいことが確定している
dp = [[[0] * 2 for _ in range(D)] for _ in range(L + 1)]
dp[0][0][0] = 1  # まだ何も選んでいないとき、和=0, まだ小さい確定はしてない

for i in range(L):  # 桁を左から順に決めていく
    k_digit = int(K[i])  # K の i 桁目
    for s in range(D):
        for t in range(2):  # フラグ 0 or 1
            val = dp[i][s][t]
            if val == 0:
                continue
            # 次の桁を d とする
            limit = 9 if t == 1 else k_digit  # フラグによって上限が違う
            for d in range(limit + 1):
                ns = (s + d) % D
                nt = t
                if t == 0:  # まだ一致中のとき
                    if d < k_digit:
                        nt = 1  # ここで小さいことが確定
                    elif d > k_digit:
                        continue  # 超えてしまうので無効
                dp[i + 1][ns][nt] = (dp[i + 1][ns][nt] + val) % MOD

# 最後に桁和 mod D == 0 のものを数える
ans = (dp[L][0][0] + dp[L][0][1] - 1) % MOD
# -1 は「0」を除くため

print(ans)
