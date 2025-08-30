import itertools


def inversion_count(perm):
    """
    順列における逆順数 (inversion count) を計算する関数。

    逆順数とは：
    順列の中で、前に出現すべきでない順序で現れる要素のペアの数のこと。
    """
    count = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                count += 1
    return count


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

# 初期状態の行と列の順番
initial_rows = list(range(H))
initial_cols = list(range(W))

min_operations = float("inf")

# 行と列の順列を全探索
for row_perm in itertools.permutations(initial_rows):
    for col_perm in itertools.permutations(initial_cols):
        # グリッド A を現在の順列で並べ替えたものを作成
        A_prime = [[A[row_perm[i]][col_perm[j]] for j in range(W)] for i in range(H)]

        # 一致するか確認
        if A_prime == B:
            # 一致する場合、操作回数を計算
            row_ops = inversion_count(row_perm)
            col_ops = inversion_count(col_perm)
            total_ops = row_ops + col_ops
            min_operations = min(min_operations, total_ops)

if min_operations == float("inf"):
    print(-1)
else:
    print(min_operations)
