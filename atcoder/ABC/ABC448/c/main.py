N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = sorted((a, i) for i, a in enumerate(A))

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    B = set(x - 1 for x in B)

    for a, idx in A:
        if idx not in B:
            print(a)
            break
