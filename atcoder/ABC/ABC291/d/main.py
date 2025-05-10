MOD = 998244353
N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i枚目のカードまでで、i枚目をj（0:表, 1:裏）にしたときの条件を満たす並べ方の総数
dp = [[0, 0] for _ in range(N)]
dp[0][0] = 1  # 1枚目を表にした場合
dp[0][1] = 1  # 1枚目を裏にした場合

for i in range(1, N):
    for prev in range(2):  # 前のカードの表裏
        for curr in range(2):  # 現在のカードの表裏
            if AB[i - 1][prev] != AB[i][curr]:
                dp[i][curr] += dp[i - 1][prev]
                dp[i][curr] %= MOD

# 最後のカードを表にした場合と裏にした場合の総数を合計
print((dp[N - 1][0] + dp[N - 1][1]) % MOD)
