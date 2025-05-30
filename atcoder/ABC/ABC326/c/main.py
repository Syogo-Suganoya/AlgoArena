import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

# プレゼントの位置をソート
A.sort()

res = 0
for i in range(N):
    # 区間の右端を求める
    right = A[i] + M
    # A[i] + M 未満の位置を二分探索で探す
    idx = bisect.bisect_left(A, right)
    # 区間に含まれるプレゼントの数を計算
    count = idx - i
    # 最大値を更新
    res = max(res, count)

print(res)
