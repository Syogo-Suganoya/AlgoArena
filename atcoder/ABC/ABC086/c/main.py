N = int(input())

now_x, now_y = 0, 0  # 現在の位置
now_t = 0  # 現在の時刻

for _ in range(N):
    t, x, y = map(int, input().split())

    # 必要な移動距離（マンハッタン距離）
    dist = abs(x - now_x) + abs(y - now_y)
    dt = t - now_t  # 残り時間

    # 条件1: 移動できる時間より距離が大きければ無理
    # 条件2: 距離と時間の偶奇が一致しないと到達できない
    if dist > dt or (dt - dist) % 2 != 0:
        print("No")
        exit()

    # 状態更新
    now_x, now_y = x, y
    now_t = t

# すべて通過できるならOK
print("Yes")
