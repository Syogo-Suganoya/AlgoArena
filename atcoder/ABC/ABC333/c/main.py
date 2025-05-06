# 入力：N番目に小さい数を求める
N = int(input())

# レピュニット（すべての桁が1の数）を格納するリスト
repunits = []
num = 0

# 1, 11, 111, ..., 12桁分までのレピュニットを作る
# 上限は問題の制約（N≦333）から十分カバーできる
for _ in range(12):
    num = num * 10 + 1  # 例: 1 → 11 → 111 → ...
    repunits.append(num)

# レピュニット3つの和をすべて列挙し、重複しないよう集合に格納
sums = set()
for i in repunits:
    for j in repunits:
        for k in repunits:
            sums.add(i + j + k)

# 集合からソートされたリストに変換して、N番目の要素を出力（0-indexなのでN-1）
result = sorted(sums)
print(result[N - 1])
