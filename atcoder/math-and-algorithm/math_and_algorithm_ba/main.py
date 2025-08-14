N = int(input())

# 2の累乗を探すための変数
num = 2

# N より大きい最小の 2 の累乗を見つける
while N > num:
    num *= 2  # 2, 4, 8, 16, ...

# N が 2^k - 1 の形なら後手勝ち
# それ以外なら先手勝ち
if num - 1 == N:
    print("Second")  # 後手勝ち
else:
    print("First")  # 先手勝ち
