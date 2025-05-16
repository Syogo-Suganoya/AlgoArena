N, M, Q = map(int, input().split())
# 荷物リスト
bags = [tuple(map(int, input().split())) for _ in range(N)]
# 箱の容量リスト
boxes = list(map(int, input().split()))

# 価値が高い順に荷物を並べ替える（価値を優先して詰めるため）
bags.sort(key=lambda x: -x[1])

for _ in range(Q):
    L, R = map(int, input().split())

    # 使用できる箱のリストを作成（L番目からR番目の箱は使用不可）
    # L, Rは1-indexなので、boxes[:L-1] と boxes[R:] で範囲外の箱を取得
    available_boxes = sorted(boxes[: L - 1] + boxes[R:])

    # 各荷物が詰められたかどうかの管理リスト。Falseはまだ詰めていないことを意味する
    used = [False] * N

    total_value = 0  # 今回のクエリで詰める荷物の合計価値を保持

    # 箱を容量の小さい順に順に処理することで、
    # 小さい箱にも詰められる荷物を優先的に探せるようにする
    for box_capacity in available_boxes:
        # 価値が高い順にソート済みの荷物リストから
        # まだ詰められていない荷物を探索
        for i in range(N):
            # 荷物の重さが箱の容量以下で、まだ使われていなければ詰める
            if not used[i] and bags[i][0] <= box_capacity:
                used[i] = True  # この荷物は使ったのでフラグを立てる
                total_value += bags[i][1]  # 価値を加算
                break  # その箱には1つしか詰められないのでループ抜ける

    print(total_value)
