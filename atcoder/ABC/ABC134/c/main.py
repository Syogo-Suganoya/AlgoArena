N = int(input())
A = [int(input()) for _ in range(N)]

# 降順ソートして最大値と2番目を求める
sorted_A = sorted(A, reverse=True)
max1 = sorted_A[0]  # 最大値
max2 = sorted_A[1]  # 2番目の値

# 各要素ごとに判定して出力
for a in A:
    if a == max1:
        print(max2)
    else:
        print(max1)
