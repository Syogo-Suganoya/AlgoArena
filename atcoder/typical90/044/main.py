from collections import deque

N, Q = map(int, input().split())
A = list(map(int, input().split()))

deq = deque(A)
for _ in range(Q):
    T, x, y = map(int, input().split())
    match T:
        case 1:
            deq[x - 1], deq[y - 1] = deq[y - 1], deq[x - 1]
        case 2:
            deq.appendleft(deq.pop())
        case 3:
            print(deq[x - 1])
