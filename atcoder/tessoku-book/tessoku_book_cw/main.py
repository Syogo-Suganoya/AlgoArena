import bisect

N = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(N)]

# 1. (X昇順, Y降順) でソート
boxes.sort(key=lambda x: (x[0], -x[1]))

# 2. Y のみ取り出す
Y_list = [y for _, y in boxes]

# 3. LIS を求める (二分探索で O(N log N))
lis = []
for y in Y_list:
    # lis 内の "y 以上の最小要素" の位置を探す
    pos = bisect.bisect_left(lis, y)
    if pos == len(lis):
        lis.append(y)
    else:
        lis[pos] = y

print(len(lis))
