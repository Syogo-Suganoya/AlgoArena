"""
累積和と二分探索を使って、その位置以上の累積和を求める
"""

import bisect

N = int(input())
A = list(map(int, input().split()))

# 数列を降順にソート
sorted_A = sorted(A, reverse=True)

# 累積和を計算
cum_sum = [0]
for val in sorted_A:
    cum_sum.append(cum_sum[-1] + val)

# 各要素に対する合計を計算
result = []
for val in A:
    # val より大きい要素の数を求める
    idx = bisect.bisect_right(sorted_A, val, lo=0, hi=N)
    result.append(cum_sum[idx])

print(" ".join(map(str, result)))
