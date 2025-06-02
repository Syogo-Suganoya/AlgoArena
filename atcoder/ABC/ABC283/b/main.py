N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    k = query[1] - 1
    match query[0]:
        case 1:
            x = query[2]
            A[k] = x
        case 2:
            print(A[k])
