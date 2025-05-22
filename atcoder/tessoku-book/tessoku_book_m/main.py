import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

res = 0

for i in range(N):
    # A[i] + 2 より小さい値のうち、何個あるか
    idx = bisect.bisect_right(A, A[i] + K)

    # i より後ろの要素の個数のみを加算
    count = max(0, idx - (i + 1))
    res += count

print(res)
