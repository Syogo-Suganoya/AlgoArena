from collections import deque

dq = deque()
q = int(input())
for i in range(q):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        [x, c] = inp[1:]
        dq.append((x, c))
    else:
        c = inp[1]
        ans = 0
        while c > 0:
            (y, d) = dq.popleft()
            ans += y * (min(d, c))
            c -= d
            if c < 0:
                dq.appendleft((y, -c))
        print(ans)
