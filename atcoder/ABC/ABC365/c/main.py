import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()

A.sort()
cumsum = [0] * (N + 1)
for i in range(N):
    cumsum[i + 1] = cumsum[i] + A[i]

# 二分探索でiの最大値を探す
left, right = 0, max(A)
res = -1
while left <= right:
    mid = (left + right) // 2
    idx = bisect.bisect_right(A, mid)
    tmp = cumsum[idx] + (N - idx) * mid
    if tmp <= M:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
