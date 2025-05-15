import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

min_diff = float("inf")

for a in A:
    idx = bisect.bisect_left(B, a)
    for j in [idx - 1, idx, idx]:
        if 0 <= j < M:
            min_diff = min(min_diff, abs(a - B[j]))

print(min_diff)
