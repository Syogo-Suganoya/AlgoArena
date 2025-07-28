import bisect

# 入力の読み込み
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 各クエリに対して処理
for _ in range(Q):
    k = int(input())

    # 二分探索の範囲を初期化
    l = 0
    r = 10**18 + 10**6

    # 二分探索
    while r - l > 1:
        m = (l + r) // 2  # 中央の候補値

        # Aの中で、m以下の値がいくつあるか（= mまでに除外された数の個数）
        excluded = bisect.bisect_right(A, m)

        # mまでに存在する「使える自然数」の個数
        valid = m - excluded

        # k個以上存在するなら、より小さいmでも条件を満たすかもしれない
        if valid >= k:
            r = m
        else:
            l = m

    # r が条件を満たす最小の数、つまり「k番目に使える自然数」
    print(r)
