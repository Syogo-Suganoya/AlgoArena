N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tl = 0
for i in range(N):
    tl += min(A[i], B[i])

for _ in range(Q):
    c, X, V = input().split()
    X = int(X) - 1
    V = int(V)
    old_min = min(A[X], B[X])

    if c == "A":
        A[X] = V
    else:
        B[X] = V

    new_min = min(A[X], B[X])

    tl += new_min - old_min

    print(tl)
