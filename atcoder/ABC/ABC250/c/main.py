N, Q = map(int, input().split())

# pos[i] は値 i のボールがどこにあるか（インデックス）
pos = list(range(N))

# val[i] はインデックス i にあるボールの値
val = list(range(N))

for _ in range(Q):
    x = int(input()) - 1  # ボール番号を 0-indexed にする

    i = pos[x]  # ボール x の現在位置

    # スワップ先を決定：末尾なら左、そうでなければ右
    if i == N - 1:
        j = i - 1
    else:
        j = i + 1

    # ボールの値を取得
    a, b = val[i], val[j]

    # スワップ
    val[i], val[j] = b, a
    pos[a], pos[b] = j, i

# 最終的な並び（val）を出力
for i in val:
    print(i + 1, end=" ")
