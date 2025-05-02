"""
アプローチ:
- 配列 A を昇順にソートしておく。
- 各クエリごとに、距離 x に対して [B - x, B + x] に含まれる A の要素数を数える関数 f(x) を定義。
- 条件 f(x) >= k を満たす最小の x を二分探索で求める。
- 距離が十分に大きい場合には必ず条件を満たすので、探索範囲は 0〜2e8 でよい。
"""

import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
results = []

for i in range(Q):
    b, k = map(int, input().split())

    # Bの±x範囲にAの要素が何個あるか
    def f(x, b, k):
        left = bisect.bisect_left(A, b - x)
        right = bisect.bisect_right(A, b + x)
        return right - left >= k

    # 二分探索で最小のxを探す
    low, high = -1, int(2e8) + 10  # highはA[i], B[j]の最大値を考慮して十分大きく
    while high - low > 1:
        mid = (low + high) // 2
        if f(mid, b, k):
            high = mid
        else:
            low = mid

    results.append(str(high))

print("\n".join(results))
