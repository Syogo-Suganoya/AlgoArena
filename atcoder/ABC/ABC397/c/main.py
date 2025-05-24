N = int(input())
A = list(map(int, input().split()))

# L[i]: 先頭からiまでの種類数
L = [0] * N
# R[i]: iから末尾までの種類数
R = [0] * N

# 左側の種類数を計算する
seen = set()  # すでに出現した整数を記録する集合
for i in range(N):
    seen.add(A[i])  # A[i]を集合に追加
    L[i] = len(seen)  # その時点での種類数

# 右側の種類数を計算する
seen.clear()  # 集合をリセット
for i in range(N - 1, -1, -1):  # 末尾から先頭に向けてループ
    seen.add(A[i])  # A[i]を集合に追加
    R[i] = len(seen)  # その時点での種類数

# 最大の種類数の和を求める
res = 0
for i in range(N - 1):  # 分割位置はN-1まで（末尾は分割できない）
    # 左部分列の種類数 + 右部分列の種類数
    res = max(res, L[i] + R[i + 1])  # 最大値を更新

print(res)  # 結果を出力
