import bisect

N, M = map(int, input().split())
H = list(map(int, input().split()))

# 累積和を作る
cumsum = [0]
for h in H:
    cumsum.append(cumsum[-1] + h)

idx = bisect.bisect_right(cumsum, M) - 1
print(idx)
