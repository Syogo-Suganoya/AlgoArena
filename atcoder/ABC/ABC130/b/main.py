import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 累積和を作る
S = [0]
for x in A:
    S.append(S[-1] + x)

# 累積和に M が含まれるか二分探索
idx = bisect.bisect_right(S, M)
print(idx)
