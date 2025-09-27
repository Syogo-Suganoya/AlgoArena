K = int(input())  # トーナメントの深さ
num = 2**K  # 参加者の人数（2^K人）
R = [int(input()) for _ in range(num)]  # 各選手のレーティング

# win_rate[i][j] : 選手 i が選手 j に勝つ確率
win_rate = [[-1] * num for _ in range(num)]
for i in range(num - 1):
    for j in range(i + 1, num):
        # Eloレーティング式で i が j に勝つ確率
        win_rate[i][j] = 1 / (1 + 10 ** ((R[j] - R[i]) / 400))
        # j が i に勝つ確率は 1 - i が j に勝つ確率
        win_rate[j][i] = 1 - win_rate[i][j]

# rem_rate[i] : 現在ラウンドまで残っている確率（初期値は全員 1）
rem_rate = [1] * num

# 各ラウンドを順に処理
for g in range(K):
    new_rem_rate = [0] * num  # 次ラウンドの残存率を格納する配列
    for i in range(num):
        # 自分がいるブロックのインデックス（ブロックサイズ = 2^g）
        if (i // (2**g)) % 2 == 0:
            # 偶数ブロックの場合、対戦相手のブロックは右隣
            enemy_left = (i // (2**g) + 1) * (2**g)
        else:
            # 奇数ブロックの場合、対戦相手のブロックは左隣
            enemy_left = (i // (2**g) - 1) * (2**g)

        # そのブロック内の全選手と対戦
        for j in range(enemy_left, enemy_left + 2**g):
            # 新しい残存率を計算
            # 自分が残っている確率 * 対戦相手が残っている確率 * 勝率
            new_rem_rate[i] += rem_rate[i] * win_rate[i][j] * rem_rate[j]

    # 次ラウンドの残存率に更新
    rem_rate = new_rem_rate

# 最終ラウンド後の勝率を出力
for i in range(num):
    print(rem_rate[i])
