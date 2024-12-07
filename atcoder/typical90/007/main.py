import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

INF = float('inf')

A.sort()

for _ in range(Q):
    B = int(input())
    pos1 = bisect.bisect_left(A, B)
    Diff1 = abs(B - A[pos1]) if pos1 < N else INF
    Diff2 = abs(B - A[pos1 - 1]) if pos1 > 0 else INF
    print(min(Diff1, Diff2))
