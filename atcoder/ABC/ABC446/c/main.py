from collections import deque

T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    l = deque()

    for i in range(N):
        l.append((i, A[i]))

        need = B[i]
        while need > 0 and l:
            idx, val = l[0]

            if val <= need:
                need -= val
                l.popleft()
            else:
                l[0] = (idx, val - need)
                need = 0

        while l and l[0][0] <= i - D:
            l.popleft()

    print(sum(val for _, val in l))
