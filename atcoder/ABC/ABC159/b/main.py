S = input().strip()
N = len(S)

# 全体が回文か
if S != S[::-1]:
    print("No")
    exit()

# 前半と後半を抽出
first_half = S[: (N - 1) // 2]
second_half = S[(N + 3) // 2 - 1 :]

# 前半が回文か
if first_half != first_half[::-1]:
    print("No")
    exit()

# 後半が回文か
if second_half != second_half[::-1]:
    print("No")
    exit()

print("Yes")
