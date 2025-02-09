MAX = pow(10, 5) + 1  # 最大の議席数の範囲
INF = pow(10, 18) + 1  # 十分大きな値（初期値として使用）


N = int(input())

dp = [INF for _ in range(MAX + 1)]  # 各議席数における最小の鞍替え人数
dp[0] = 0  # 0議席は0人の鞍替えで達成可能
sum_Z = 0  # 議席の合計

for i in range(N):
    X, Y, Z = map(int, input().split())  # i番目の選挙区の情報を取得
    sum_Z += Z  # 総議席数を加算

    next_dp = [INF for _ in range(MAX + 1)]  # 次の状態を保持する配列

    for z in range(MAX - Z):  # 遷移前の状態を走査
        if dp[z] == INF:  # INFならば遷移できないのでスキップ
            continue

        if X > Y:  # すでに高橋君が勝っているなら
            next_dp[z + Z] = min(next_dp[z + Z], dp[z])  # そのまま議席を追加
        else:  # 高橋君が負けているなら
            # 鞍替えさせない場合（そのまま）
            next_dp[z] = min(next_dp[z], dp[z])

            # 鞍替えして勝つ場合
            target = (X + Y) // 2 + 1  # 過半数を超えるための必要な票数
            next_dp[z + Z] = min(next_dp[z + Z], dp[z] + max(0, target - X))

    dp = next_dp  # 次の状態に更新


ans = min(dp[(sum_Z // 2 + 1) :])  # 過半数を超えるための最小の鞍替え人数を取得
print(ans)
