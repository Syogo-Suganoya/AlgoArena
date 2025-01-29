N = int(input())
A = list(map(int, input().split()))

Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            k, x = query[1:]
            A[k - 1] = x
        case 2:
            k = query[1]
            print(A[k - 1])
