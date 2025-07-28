N = int(input())
T = list(map(int, input().split()))
total = sum(T)

# dp[i] = 調理時間 i を作れるかどうか
dp = [False] * (total + 1)
dp[0] = True

# 各料理を使ってDP更新（01ナップサック）
for t in T:
    for i in range(total, t - 1, -1):
        if dp[i - t]:
            dp[i] = True

# total // 2 以上の中で、最小の i を見つける
for i in range((total + 1) // 2, total + 1):
    if dp[i]:
        print(i)
        break
