N = int(input())
A = list(map(int, input().split()))

# ソートして中央値を取得
sorted_A = sorted(A)
half = N // 2
lower_median = sorted_A[half - 1]
upper_median = sorted_A[half]

# 各値に対して条件に応じて出力
for x in A:
    if x < upper_median:
        print(upper_median)
    else:
        print(lower_median)
