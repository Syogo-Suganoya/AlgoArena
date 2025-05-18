from itertools import combinations

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

# 全ての2つ組み合わせを調べる
for x, y in combinations([a, b, c, d, e], 2):
    if y - x > k:  # 差がkを超えていれば
        print(":(")  # 条件を満たさない
        exit()  # 即終了

# 全てのペアで差がk以下だった場合
print("Yay!")
