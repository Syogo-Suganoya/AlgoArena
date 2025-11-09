T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()

    # ビットDP用配列: reachable[mask] = mask 状態に到達可能か
    # mask は薬品集合をビットで表す (0 = 何も入っていない)
    reachable = [False] * (1 << N)
    reachable[0] = True  # 何も入れていない状態は安全

    # mask を順に処理して、次の状態に遷移できるか判定
    for mask in range(1 << N):
        if not reachable[mask]:
            continue  # 現在の状態がそもそも到達不可能ならスキップ

        # まだビンに入れていない薬品 k を追加して新しい集合を作る
        for k in range(N):
            if mask & (1 << k):
                continue  # 既に入っている薬品はスキップ

            new_mask = mask | (1 << k)  # 新しい集合
            # new_mask が安全かチェック
            if S[new_mask - 1] == "0":
                reachable[new_mask] = True  # 到達可能にする

    # 最終状態（すべての薬品が入った状態）に到達できるか
    if reachable[(1 << N) - 1]:
        print("Yes")
    else:
        print("No")
