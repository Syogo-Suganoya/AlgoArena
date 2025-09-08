N = int(input())
for _ in range(N):
    A, B, C = map(int, input().split())

    abc = min(A, B, C)
    A -= abc
    B -= abc
    C -= abc

    extra = min(min(A, C), (A + C) // 3)

    print(abc + extra)
