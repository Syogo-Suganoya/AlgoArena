from sortedcontainers import SortedList

Q = int(input())

# 昇順に管理
sl = SortedList()

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        sl.add(x)  # O(log N)

    elif query[0] == 2:
        x, k = query[1], query[2]
        # x 以下の中で大きい方 k 番目
        idx = sl.bisect_right(x)  # x より大きい最初の位置
        if idx - k >= 0:
            print(sl[idx - k])
        else:
            print(-1)

    else:
        x, k = query[1], query[2]
        # x 以上の中で小さい方 k 番目
        idx = sl.bisect_left(x)  # x 以上の最初の位置
        if idx + k - 1 < len(sl):
            print(sl[idx + k - 1])
        else:
            print(-1)
