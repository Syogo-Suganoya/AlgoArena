P, Q = input().split()

# A〜Z を 1〜26 に変換する（ord('A') = 65 なので、-64 すれば A=1 になる）
P = ord(P) - ord("A")
Q = ord(Q) - ord("A")

# π の最初の6桁のリスト（整数）
pi_digits = [3, 1, 4, 1, 5, 9]

# 累積和を前計算する（0番目は0）
cumsum = [0]
for num in pi_digits:
    cumsum.append(cumsum[-1] + num)

# P, Q を昇順にソート（範囲の小さい方から大きい方）
P, Q = sorted((P, Q))

# 累積和を使って、P番目〜Q-1番目までの和を求める
print(cumsum[Q] - cumsum[P])
