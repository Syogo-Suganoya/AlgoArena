N = int(input())

A = []
B = []

# 全ての範囲 [Ai, Bi] を読み込む
for _ in range(N):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)

# 最小値のリストと最大値のリストをそれぞれ独立にソートする
# これにより、それぞれの場合の中央値を特定できる
A.sort()
B.sort()

if N % 2 == 1:
    # 奇数の場合：真ん中の要素がそのまま中央値
    # 0-indexed なので、インデックスは (N-1)//2
    idx = (N - 1) // 2

    min_median = A[idx]
    max_median = B[idx]

    # 範囲内の整数の個数を出力
    print(max_median - min_median + 1)

else:
    # 偶数の場合：真ん中の2つの要素の平均が中央値
    # 0-indexed なので、インデックスは N//2 - 1 と N//2
    idx1 = N // 2 - 1
    idx2 = N // 2

    # 中央値そのものではなく「中央値の2倍」の値（2つの要素の和）で考える
    # これにより0.5刻みの値を整数として扱える
    min_val_sum = A[idx1] + A[idx2]
    max_val_sum = B[idx1] + B[idx2]

    # 範囲内の値の個数を出力
    print(max_val_sum - min_val_sum + 1)
