import bisect

N, L = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# L 以上の最初のインデックス
idx = bisect.bisect_left(A, L)
print(N - idx)
