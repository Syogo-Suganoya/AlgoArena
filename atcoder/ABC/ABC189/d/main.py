N = int(input())
S = [input().strip() for _ in range(N)]

# dp_true[i] = i 個目までの式が True になる割り当て数
# dp_false[i] = i 個目までの式が False になる割り当て数
dp_true = 1  # X1=True
dp_false = 1  # X1=False

for op in S:
    if op == "AND":
        # True を作るためには左も右も True
        new_true = dp_true
        # False は3通りから作られる
        new_false = dp_false * 2 + dp_true
    else:  # OR
        # True は3通り
        new_true = dp_true * 2 + dp_false
        # False は両方 False のときのみ
        new_false = dp_false

    dp_true, dp_false = new_true, new_false

print(dp_true)
