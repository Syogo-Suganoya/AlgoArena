N = int(input())
A = list(map(int, input().split()))

count = 0  # 条件を満たす (i, j) の組の総数
fixed_points = 0  # a[i] == i+1 となる i の数（1-indexedで一致しているもの）

for i in range(N):
    if A[i] == i + 1:
        # a[i] == i+1 のとき、固定点としてカウント（自己一致している要素）
        fixed_points += 1
    elif A[i] > i + 1 and A[A[i] - 1] == i + 1:
        # a[i] = j+1 かつ a[j] = i+1 を満たすような（対称な）ペアを探す
        # ただし i < j のときに限ってカウントする
        count += 1

# 固定点同士のペアはどの2つを選んでも条件を満たすので、組み合わせ数を加算
# fixed_points 個から2つ選ぶ組み合わせ（nC2）
count += fixed_points * (fixed_points - 1) // 2

print(count)
