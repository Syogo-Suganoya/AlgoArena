import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# 累積和を作成
cum = [0]
for v in A:
    cum.append(cum[-1] + v)

# クエリ処理
for _ in range(Q):
    x = int(input())
    idx = bisect.bisect_right(cum, x)
    print(idx - 1)
