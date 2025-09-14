def brick_break(A):
    next_needed = 1
    removed = 0
    for a in A:
        if a == next_needed:
            next_needed += 1
        else:
            removed += 1
    if next_needed == 1:
        return -1
    else:
        # 残せた数は next_needed - 1 個
        # 削除する数は全部 N 個から残せるものを引いたもの
        return removed


# 入力読み込み
N = int(input())
A = list(map(int, input().split()))
print(brick_break(A))
