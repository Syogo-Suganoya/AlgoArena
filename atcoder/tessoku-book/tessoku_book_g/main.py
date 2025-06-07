D = int(input())  # 全体の日数
N = int(input())  # 区間の数

# 長さ D+1 の配列（0-indexed でR+1の処理をするため）
imos = [0] * (D + 2)  # D+2にして、R=Dのときも大丈夫なようにしておく

for _ in range(N):
    L, R = map(int, input().split())
    imos[L] += 1  # 区間の開始点で +1
    imos[R + 1] -= 1  # 区間の終了点の次で -1

# 累積和をとって最終的な出席数に変換
for i in range(1, D + 1):
    imos[i] += imos[i - 1]

# 結果を出力（1〜D日目まで）
for i in range(1, D + 1):
    print(imos[i])
