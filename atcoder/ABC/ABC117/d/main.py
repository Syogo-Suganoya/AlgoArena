N, K = map(int, input().split())
A = list(map(int, input().split()))

MAX_BITS = 50  # 余裕をもって50ビット

# dp[d][tight]：dビット目から下で tight の状態のときの最大値
dp = [[-1] * 2 for _ in range(MAX_BITS + 1)]
dp[45][0] = 0  # 上位ビットから開始

for d in range(44, -1, -1):
    mask = 1 << d
    num = sum(1 for a in A if a & mask)

    # tight == 1（すでにKより小さい場合）
    if dp[d + 1][1] >= 0:
        dp[d][1] = max(dp[d][1], dp[d + 1][1] + mask * max(num, N - num))

    # tight == 0（まだKに一致している場合）
    if dp[d + 1][0] >= 0:
        if K & mask:
            # このビットを1にすると tight状態になる
            dp[d][1] = max(dp[d][1], dp[d + 1][0] + mask * num)
            # このビットを0にすると tightのまま
            dp[d][0] = max(dp[d][0], dp[d + 1][0] + mask * (N - num))
        else:
            # このビットは0しか選べない
            dp[d][0] = max(dp[d][0], dp[d + 1][0] + mask * num)

print(max(dp[0][0], dp[0][1]))
