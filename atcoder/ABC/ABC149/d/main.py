N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

# 手を数字で管理
hand_map = {"r": 0, "s": 1, "p": 2}
score_map = [P, R, S]  # r(0)->P, s(1)->R, p(2)->Sの得点対応

ans = 0
for start in range(K):
    group = [hand_map[T[i]] for i in range(start, N, K)]
    M = len(group)

    # dp[i][j]: i番目まで見てjの手で終わったときの最大得点
    dp = [[-1] * (3) for _ in range(M + 1)]
    for j in range(3):
        dp[0][j] = 0

    for i in range(M):
        for prev_hand in range(3):
            if dp[i][prev_hand] < 0:
                continue
            for curr_hand in range(3):
                # 連続して同じ手は禁止
                if i > 0 and curr_hand == prev_hand:
                    # 連続禁止なので得点0で遷移
                    val = dp[i][prev_hand]
                else:
                    val = dp[i][prev_hand] + (
                        score_map[curr_hand] if curr_hand == group[i] else 0
                    )
                dp[i + 1][curr_hand] = max(dp[i + 1][curr_hand], val)

    ans += max(dp[M])

print(ans)
