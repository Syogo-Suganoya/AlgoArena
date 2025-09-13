N = input().strip()
K = int(input())
L = len(N)

# dp[pos][cnt][tight]
dp = [[[0] * 2 for _ in range(K + 1)] for _ in range(L + 1)]
dp[0][0][1] = 1  # 初期状態

for pos in range(L):
    for cnt in range(K + 1):
        for tight in range(2):
            if dp[pos][cnt][tight] == 0:
                continue
            limit = int(N[pos]) if tight else 9
            for d in range(limit + 1):
                no = cnt + (1 if d != 0 else 0)
                if no > K:
                    continue
                ntight = tight and (d == limit)
                dp[pos + 1][no][ntight] += dp[pos][cnt][tight]

# 結果：最後の pos = L, cnt = K, tight = 0 or 1 の合計
res = dp[L][K][0] + dp[L][K][1]
print(res)
