from sortedcontainers import SortedList

l = SortedList()

N = int(input())
for _ in range(N):
    q, x = map(int, input().split())
    match q:
        case 1:
            l.add(x)
        case 2:
            l.remove(x)
        case 3:
            idx = l.bisect_left(x)
            if idx == len(l):
                print(-1)
            else:
                print(l[idx])
