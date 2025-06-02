N, X = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

# dp[j] := j円を作れるかどうかを示す真偽値
# 最初は0円だけ作れる
dp = [False] * (X + 1)
dp[0] = True

# 各硬貨ごとに遷移を考える
for a, b in AB:
    # 新しいdp配列を作成。これを更新していく。
    new_dp = dp[:]

    # 現在のdp配列を確認し、Trueならその金額jからaを1枚以上使って遷移させる
    for j in range(X + 1):
        if dp[j]:
            # 1枚からb枚まで使って遷移
            for k in range(1, b + 1):
                nxt = j + a * k
                if nxt > X:
                    break  # 上限を超えたら打ち切り
                new_dp[nxt] = True  # nxt円を作れることを記録

    # dp配列を更新
    dp = new_dp

# X円を作れるかどうかを出力
print("Yes" if dp[X] else "No")
