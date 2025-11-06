import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
prefix = [0]
for a in A:
    prefix.append(prefix[-1] + a)

total = prefix[-1]  # sum(A)

for i in range(Q):
    B = int(input())

    # B_j - 1 以下の値の個数を探す（二分探索）
    idx = bisect.bisect_right(A, B - 1)

    # sum(min(A_i, b-1)) = sum(A_i < b) + (b-1)*残り個数
    sum_min = prefix[idx] + (B - 1) * (N - idx)

    # 勝てるための最小x
    x = sum_min + 1

    # 不可能条件
    if A[-1] < B or x > total:
        print(-1)
    else:
        print(x)
