"""
サイコロAとBの各目の出現確率から、
AとBで「同じ目が出る」確率が最大になるサイコロの組み合わせを見つける。

共通の目の出現確率を計算し、その和が最大のペアを求める。
"""

from collections import Counter

N = int(input())
dice = []

# 各サイコロごとに、出目の種類と出現頻度を記録する
for _ in range(N):
    data = list(map(int, input().split()))
    K = data[0]  # サイコロの面数
    faces = data[1:]  # サイコロの出目リスト
    freq = Counter(faces)  # 各出目が何回出現するかをカウント
    dice.append((K, freq))  # サイコロを (面数, 出目の頻度) で保存

max_prob = 0.0

# 全てのサイコロのペアについて調べる
for i in range(N):
    K_i, freq_i = dice[i]
    for j in range(i + 1, N):
        K_j, freq_j = dice[j]

        # i番目とj番目のサイコロで共通している出目を探す
        common = set(freq_i.keys()) & set(freq_j.keys())

        prob = 0.0
        # 共通する出目ごとに確率を計算
        for x in common:
            # 出目xがサイコロiで出る確率 × サイコロjで出る確率
            prob += (freq_i[x] / K_i) * (freq_j[x] / K_j)

        # 今までの最大確率と比較して更新
        max_prob = max(max_prob, prob)

# 小数点15桁で出力
print(f"{max_prob:.15f}")
