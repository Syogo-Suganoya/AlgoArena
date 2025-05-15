import bisect

# 入力を受け取る
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# ソート（これが非常に重要。二分探索はソート済みの配列に対して使う）
A.sort()

# クエリを処理
for _ in range(Q):
    x = int(input())
    # x 以上の値が最初に現れる位置を探す（左側の境界）
    idx = bisect.bisect_left(A, x)

    # x 以上の要素数は N - idx 個
    print(N - idx)
