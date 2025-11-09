T = int(input())

for _ in range(T):
    # 入力を取得
    n, m = map(int, input().split())

    # AとBを読み込み、Aは大きい順に、Bは小さい順にソート
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())))

    # c: 条件を満たすペアの数、idx: Bの現在位置
    c, idx = 0, 0

    # Aの要素を順番に処理
    for v in a:
        # Bの中で v と足して m 以上になる最小の値を見つける
        while idx < n and b[idx] + v < m:
            idx += 1
        # Bをすべて見ても条件を満たすものがなければ終了
        if idx >= n:
            break
        # 条件を満たすペアが見つかったのでカウント
        c += 1
        # Bの次の要素に進む
        idx += 1

    # 答え: AとBの合計から m*c を引く
    # → 条件を満たすペアの数だけ m を差し引く
    print(sum(a) + sum(b) - m * c)
