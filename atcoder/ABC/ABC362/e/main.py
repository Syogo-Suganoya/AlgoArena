from collections import defaultdict

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

# dp[i][d][length] = 個数
dp = [defaultdict(lambda: defaultdict(int)) for _ in range(N)]

# 長さごとの答えをまとめる
ans = [0] * (N + 1)

# 長さ1の部分列（単独要素）は必ずある
ans[1] = N % MOD

for i in range(N):
    for j in range(i):
        d = A[i] - A[j]

        # jで終わるものをすべて伸ばす
        for length, cnt in dp[j][d].items():
            val = cnt % MOD
            dp[i][d][length + 1] = (dp[i][d][length + 1] + val) % MOD
            ans[length + 1] = (ans[length + 1] + val) % MOD

        # 新しい長さ2を作る
        dp[i][d][2] = (dp[i][d][2] + 1) % MOD
        ans[2] = (ans[2] + 1) % MOD

print(*[x % MOD for x in ans[1:]])
