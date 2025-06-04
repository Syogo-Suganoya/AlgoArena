N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[0][i]: i番目に A[i] を選べるか
# dp[1][i]: i番目に B[i] を選べるか
dp = [[False] * N for _ in range(2)]

# 初期値: 最初の位置はどちらも選べる
dp[0][0] = True
dp[1][0] = True

# 各ステップ i で、次の位置 i+1 に遷移できるかを調べる
for i in range(1, N):
    # 前の位置で A[i-1] を選んでいた場合の遷移
    if dp[0][i - 1]:
        if abs(A[i - 1] - A[i]) <= K:
            dp[0][i] = True
        if abs(A[i - 1] - B[i]) <= K:
            dp[1][i] = True

    # 前の位置で B[i-1] を選んでいた場合の遷移
    if dp[1][i - 1]:
        if abs(B[i - 1] - A[i]) <= K:
            dp[0][i] = True
        if abs(B[i - 1] - B[i]) <= K:
            dp[1][i] = True

# 最後の位置で A または B を選べていれば OK
if dp[0][N - 1] or dp[1][N - 1]:
    print("Yes")
else:
    print("No")
