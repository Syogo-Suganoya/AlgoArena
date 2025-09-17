N = int(input())  # 抵抗の数
A = list(map(int, input().split()))  # 各抵抗の値

# 逆数の和を計算
reciprocal_sum = sum(1 / a for a in A)

# 合成抵抗を計算
R = 1 / reciprocal_sum

# 結果を出力
print(R)
