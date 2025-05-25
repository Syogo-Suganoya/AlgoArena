import bisect

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = int(input())

# P の累積和を作成する
cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + P[i]

# クエリの処理
for _ in range(Q):
    L, R = map(int, input().split())

    # X の中で L 以上の最小のインデックス (左端) を探す
    left = bisect.bisect_left(X, L)

    # X の中で R 以下の最大のインデックス (右端) を探す
    right = bisect.bisect_right(X, R)

    # 累積和から範囲の合計を出力
    ans = cum[right] - cum[left]
    print(ans)

"""
N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = int(input())
Pの累積和

for i in range(Q):
    L, R = map(int, input().split())
    from=Xから二分探索left
    to=Xから二分探索right
    累積和からto-fromを出力
"""
