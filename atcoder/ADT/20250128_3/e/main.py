from sortedcontainers import SortedSet

Q = int(input())

cylinder = {}
s = SortedSet()
for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x = query[1]
            if x in cylinder:
                cylinder[x] += 1
            else:
                cylinder[x] = 1
                s.add(x)
        case 2:
            x, c = query[1:]
            if x not in cylinder:
                continue
            cylinder[x] = max(0, cylinder[x] - c)
            if cylinder[x] == 0:
                del cylinder[x]
                s.discard(x)
        case 3:
            print(s[-1] - s[0])
