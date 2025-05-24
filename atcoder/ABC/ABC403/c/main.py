N, M, Q = map(int, input().split())

# N個のセットのリストを作る
l = [set() for _ in range(N + 1)]

for _ in range(Q):
    query = list(map(int, input().split()))

    match query[0]:
        case 1:
            X, Y = query[1], query[2]
            l[X].add(Y)
        case 2:
            X = query[1]
            l[X].add(-1)
        case 3:
            X, Y = query[1], query[2]
            f = any(x in l[X] for x in (Y, -1))
            print("Yes" if f else "No")
