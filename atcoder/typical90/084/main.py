from itertools import groupby


def arithmetic_sum(a, d, n):
    return n * (2 * a + (n - 1) * d) // 2


def count_intervals(N, S):
    total_intervals = arithmetic_sum(1, 1, N)  # 1からNまでの等差数列の合計

    # ランレングス圧縮で同じ文字の連続区間の長さを取得
    rle = [(k, len(list(g))) for k, g in groupby(S)]

    # 同じ文字の区間の合計を計算
    same_char_intervals = 0
    for _, length in rle:
        same_char_intervals += arithmetic_sum(1, 1, length)

    result = total_intervals - same_char_intervals
    return result


# 入力例
N = int(input())
S = input()
print(count_intervals(N, S))
