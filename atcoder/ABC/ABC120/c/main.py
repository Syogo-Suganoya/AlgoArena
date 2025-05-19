S = input()

# 文字列中の '0' の個数を数える
count_0 = S.count("0")

# 文字列中の '1' の個数を数える
count_1 = S.count("1")

# '0' と '1' の少ない方の個数を求める
min_count = min(count_0, count_1)

# 削除される文字数の合計は、ペア数 × 2
result = 2 * min_count

print(result)
