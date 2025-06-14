N = int(input())
events = []

L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

L.sort()
R.sort()
no_cross = 0
j = 0
for l in L:
    while j < N and R[j] < l:
        j += 1
    no_cross += j

total_pairs = N * (N - 1) // 2
answer = total_pairs - no_cross
print(answer)


def ano():
    N = int(input())
    events = []

    for _ in range(N):
        l, r = map(int, input().split())
        events.append((l, 1))  # 開始点
        events.append((r, -1))  # 終了点

    # イベントを位置で昇順に、同じ位置の場合は開始点が先になるようにソート
    events.sort(key=lambda x: (x[0], -x[1]))

    open_intervals = 0
    ans = 0

    for _, event_type in events:
        if event_type == 1:
            # 現在開いている区間の数を答えに加算
            ans += open_intervals
            open_intervals += 1
        else:
            open_intervals -= 1

    print(ans)
