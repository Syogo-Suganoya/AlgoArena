Q = int(input())
l = [0] * 100

for _ in range(Q):
    query = list(map(int, input().split()))

    match query[0]:
        case 1:
            X = query[1]
            l.append(X)
        case 2:
            print(l.pop())
