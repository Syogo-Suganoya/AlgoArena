from collections import deque

Q = int(input())
queue = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x, c = query[1:]
            queue.append([x, c])
        case 2:
            c = query[1]
            total = 0
            while queue and c > 0:
                x, count = queue[0]
                if count <= c:
                    total += x * count
                    c -= count
                    queue.popleft()
                    continue
                total += x * c
                queue[0][1] -= c
                c = 0
            print(total)
