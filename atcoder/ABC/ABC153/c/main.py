N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
if K >= 1:
    A = A[:-K]
print(sum(A))
