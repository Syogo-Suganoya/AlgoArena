H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
transpose = [[row[i] for row in A] for i in range(W)]
for i in transpose:
    print(*i)
