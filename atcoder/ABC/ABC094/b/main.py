import bisect

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

# X未満の要素がいくつあるか（二分探索で取得）
idx = bisect.bisect_left(A, X)

# 左から行く場合 → A[0]〜A[idx-1] の料金所を通る
# 右から行く場合 → A[idx]〜A[-1] の料金所を通る
left_cost = idx
right_cost = M - idx

# 少ない方を選ぶ
print(min(left_cost, right_cost))
