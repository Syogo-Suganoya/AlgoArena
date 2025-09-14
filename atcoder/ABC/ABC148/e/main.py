def count_trailing_zeros_double_factorial(N):
    # N が奇数なら 0 を返す
    if N % 2 == 1:
        return 0

    # N を 2 で割った商を M にする
    M = N // 2

    # 5 の因子の数を数える
    zeros = 0
    while M > 0:
        M //= 5
        zeros += M

    return zeros


# 入力を読んで答えを出力
N = int(input().strip())
print(count_trailing_zeros_double_factorial(N))
