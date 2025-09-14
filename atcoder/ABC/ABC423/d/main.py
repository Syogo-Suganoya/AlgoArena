from heapq import heappop, heappush

N, K = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

cur = 0
heap = []  # 退店イベント (退店時刻, 人数)
entered = -1  # 直前の入店時間

for idx, (a, b, c) in enumerate(ABC):
    t = max(a, entered)  # 入店希望時間 or 前回入店時間以降

    # 空席ができるまで退店処理
    while cur + c > K:
        out_time, out_c = heappop(heap)
        cur -= out_c
        # 時間を 次の退店 か 入店希望時間 or 前回入店時間以降 に進める
        t = max(t, out_time)
        # この時間までに退店すべき人をまとめて処理
        while heap and heap[0][0] <= t:
            ot, oc = heappop(heap)
            cur -= oc

    # 入店処理
    entered = t
    print(entered)  # 最小入店可能時刻
    cur += c
    heappush(heap, (t + b, c))
