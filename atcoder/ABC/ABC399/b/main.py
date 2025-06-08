import bisect

N = int(input())
A = list(map(int, input().split()))

# ソートした配列を作成（元の A を変更しないようにコピー）
sa = sorted(A)

# 各要素の順位を求めて出力
for a in A:
    # 二分探索で a の位置を取得（0-indexed）
    idx = bisect.bisect_right(sa, a)
    print(N - idx + 1)
