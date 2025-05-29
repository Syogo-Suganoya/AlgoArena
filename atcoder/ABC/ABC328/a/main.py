import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

idx = bisect.bisect_right(A, X)
res = sum(A[:idx])
print(res)
