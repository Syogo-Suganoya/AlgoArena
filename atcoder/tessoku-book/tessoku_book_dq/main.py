N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
for i in range(Q):
    q, x, y = map(int, input().split())
    x -= 1
    y -= 1
    match q:
        case 1:
            A[x], A[y] = A[y], A[x]
        case 2:
            print(A[x][y])
