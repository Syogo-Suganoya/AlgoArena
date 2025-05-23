from itertools import product

N = int(input())

# 10桁の4,7のラッキー数を全列挙
lucky_numbers = []
for digits in product(["4", "7"], repeat=10):
    num = int("".join(digits))
    lucky_numbers.append(num)

# 昇順にソートしてN番目を取得（1-indexed）
lucky_numbers.sort()
print(lucky_numbers[N - 1])
