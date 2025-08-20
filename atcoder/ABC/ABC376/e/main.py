import heapq

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # AとBをペアにしてAの小さい順にソート
    # （「このaを最大値にする」候補を順番に試すため）
    C = sorted([(a, b) for a, b in zip(A, B)])

    ans = 10**18  # 最小値を記録する変数（大きな値で初期化）

    Q = []  # 選んだbを格納するヒープ
    bsum = 0  # ヒープに入っているbの合計

    for i in range(N):
        a, b = C[i]  # 今見ている (a, b)

        # 「このaを最大にする」と仮定した場合、
        # すでにK-1個のbが選ばれていれば、答えを更新できる
        if len(Q) == K - 1:
            ans = min(ans, a * (bsum + b))

        # bをヒープに追加する
        # Pythonのheapqは最小ヒープなので、-bで「最大ヒープ」にして管理
        heapq.heappush(Q, -b)
        bsum += b  # 合計値を更新

        # ヒープのサイズがK-1を超えたら、一番大きいbを取り除く
        # （「bの和をできるだけ小さくしたい」ため）
        if len(Q) > K - 1:
            bsum -= -heapq.heappop(Q)

    print(ans)
