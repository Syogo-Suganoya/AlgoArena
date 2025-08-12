N, A, B = map(int, input().split())

dp = [False] * (N + 1)
# dp[0] = False は初期値のまま（石0は負け）

for j in range(1, N + 1):
    # A個取れるかつ相手が負けなら自分は勝ち
    if j - A >= 0 and not dp[j - A]:
        dp[j] = True
    # B個取れるかつ相手が負けなら自分は勝ち
    elif j - B >= 0 and not dp[j - B]:
        dp[j] = True

print("First" if dp[N] else "Second")
