import bisect

N, H, X = map(int, input().split())
A = list(map(int, input().split()))

d = X - H
idx = bisect.bisect_left(A, d)
print(idx + 1)
