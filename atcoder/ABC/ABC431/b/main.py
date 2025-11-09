X = int(input())
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

flag = [False] * N

for _ in range(Q):
    P = int(input()) - 1

    if not flag[P]:
        X += A[P]
        flag[P] = True
    else:
        X -= A[P]
        flag[P] = False

    print(X)
