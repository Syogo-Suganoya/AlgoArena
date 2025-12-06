from sortedcontainers import SortedList

N, Q = map(int, input().split())

intervals = SortedList()
total_len = 0

for _ in range(Q):
    l, r = map(int, input().split())

    nl, nr = l, r
    idx = intervals.bisect_left([l, r])
    merge_indices = []

    if idx - 1 >= 0:
        a, b = intervals[idx - 1]
        if b >= l:
            merge_indices.append(idx - 1)

    j = idx
    while j < len(intervals):
        a, b = intervals[j]
        if a > nr:
            break
        merge_indices.append(j)
        j += 1

    for k in reversed(merge_indices):
        a, b = intervals[k]
        total_len -= b - a + 1
        nl = min(nl, a)
        nr = max(nr, b)
        intervals.pop(k)

    intervals.add([nl, nr])
    total_len += nr - nl + 1

    print(N - total_len)
