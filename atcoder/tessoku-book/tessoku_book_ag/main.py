# 入力
N = int(input())
A = list(map(int, input().split()))

# ニム和を計算
nim_sum = 0
for a in A:
    nim_sum ^= a  # XOR

# 判定
if nim_sum == 0:
    print("Second")  # 後手勝ち
else:
    print("First")  # 先手勝ち
