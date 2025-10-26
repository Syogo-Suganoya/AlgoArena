N, M = map(int, input().split())
for i in range(N):
    if i + 1 <= M:
        print("OK")
    else:
        print("Too Many Requests")
