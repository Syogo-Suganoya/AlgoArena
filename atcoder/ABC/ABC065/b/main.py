N = int(input())
A = [int(input()) for _ in range(N)]
s = set()
now = 1
c = 0
while True:
    now = A[now - 1]
    c += 1

    if now == 2:
        print(c)
        break
    if now in s:
        print(-1)
        break
    s.add(now)
