from heapq import heappop, heappush

N, K = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

cur = 0
heap = []
entered = -1

for idx, (a, b, c) in enumerate(ABC):
    if idx == 0:
        t = a
    else:
        t = max(a, entered)

    # 退店
    while heap and heap[0][0] <= t:
        out_time, out_c = heappop(heap)
        cur -= out_c

    # 入店できるまで退店を進める
    while cur + c > K:
        out_time, out_c = heappop(heap)
        cur -= out_c
        t = max(t, out_time)
        # 退店
        while heap and heap[0][0] <= t:
            ot, oc = heappop(heap)
            cur -= oc

    entered = t
    print(entered)
    cur += c
    heappush(heap, (t + b, c))
