from collections import deque

deq = deque()

Q = int(input())
for _ in range(Q):
    t, x = map(int, input().split())
    match t:
        case 1:
            deq.appendleft(x)
        case 2:
            deq.append(x)
        case 3:
            print(deq[x - 1])
