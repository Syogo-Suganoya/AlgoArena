# 入力
N, W, C = map(int, input().split())  # N: 品物数, W: 最大重量, C: 最大色数
WV = [[] for _ in range(50)]  # 色ごとの品物リスト（0-indexed）
for _ in range(N):
    w, v, c = map(int, input().split())
    WV[c - 1].append((w, v))  # 品物をその色のリストに追加

inf = float("inf")
# dp[i][j] := 色を i 個使い、重さ j 以下で得られる最大価値
dp = [[-inf] * (W + 1) for _ in range(C + 1)]
dp[0][0] = 0  # 色0, 重さ0 のとき価値0

# 色ごとに処理
for c in range(50):
    # ndp は新しい色を追加したときの DP
    ndp = [[-inf] * (W + 1) for _ in range(C + 1)]

    # 現在の色 c の各品物を試す
    for w, v in WV[c]:
        # i: これまで使った色数（後ろから更新で重複防止）
        for i in range(C):
            # j: 重さ（後ろから更新して品物の重複を避ける）
            for j in range(W - w, -1, -1):
                # ndp[i+1][j+w] に更新
                # i+1 → 新しい色を1つ追加した状態
                # j+w → 現在の重さに品物の重さを加えた
                # max(ndp[i+1][j], dp[i][j]) + v → 既存状態 or dp を選択
                ndp[i + 1][j + w] = max(
                    ndp[i + 1][j + w], max(ndp[i + 1][j], dp[i][j]) + v
                )

    # ndp の結果を dp に反映
    for i in range(C + 1):
        for j in range(W + 1):
            dp[i][j] = max(dp[i][j], ndp[i][j])

# 最終的に dp の全体で最大値を取る
ans = 0
for i in range(C + 1):
    ans = max(ans, max(dp[i]))
print(ans)
