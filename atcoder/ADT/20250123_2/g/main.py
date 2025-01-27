from sortedcontainers import SortedList

# 空の SortedList を作成
sequence = SortedList()

N = int(input())

for _ in range(N):
    q = input().split()
    match q[0]:
        case "1":
            x = int(q[1])
            sequence.add(x)
        case "2":
            x, k = int(q[1]), int(q[2])
            idx = sequence.bisect_right(x)
            if idx >= k:
                print(sequence[idx - k])
            else:
                print(-1)
        case "3":
            x, k = int(q[1]), int(q[2])
            idx = sequence.bisect_left(x)
            if len(sequence) - idx >= k:
                print(sequence[idx + k - 1])
            else:
                print(-1)
