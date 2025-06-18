N = int(input())

count = 0

# 奇数だけ調べる → 2ずつ増やす
for num in range(1, N + 1, 2):
    divisor_count = 0

    # 1 から num までのすべての数で割ってみる
    for i in range(1, num + 1):
        if num % i == 0:
            divisor_count += 1

    # ちょうど8個の約数がある数をカウント
    if divisor_count == 8:
        count += 1

print(count)
