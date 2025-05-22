import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))
print(bisect.bisect_left(A, X) + 1)
