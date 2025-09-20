import heapq

T = int(input())
for _ in range(T):
    N, K, X = map(int, input().split())
    A = list(map(float, input().split()))  # 長さは float

    # 最大ヒープとして管理するため負の値で heapq を使う
    pq = []
    for a in A:
        heapq.heappush(pq, (-a, 1))  # (長さ, 本数)

    # K 回の操作を行う
    k_remaining = K
    while k_remaining:
        a, count = heapq.heappop(pq)
        a = -a  # 元の値に戻す
        if k_remaining <= count:
            # K 回以内で操作が終わる場合
            heapq.heappush(pq, (-(a / 2), k_remaining * 2))
            if count - k_remaining > 0:
                heapq.heappush(pq, (-a, count - k_remaining))
            k_remaining = 0
            break
        else:
            # 全部半分にする
            heapq.heappush(pq, (-(a / 2), count * 2))
            k_remaining -= count

    # 大きい順に X 番目を求める
    x_remaining = X
    while pq:
        a, count = heapq.heappop(pq)
        a = -a
        if x_remaining <= count:
            print(a)
            break
        x_remaining -= count
