N = int(input())
A = [input() for _ in range(N)]

# "For" の個数をカウント
count_for = A.count("For")

# 半分より多い（N // 2 より大きい）なら Yes
if count_for >= (N // 2 + 1):
    print("Yes")
else:
    print("No")
