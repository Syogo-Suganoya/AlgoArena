from collections import Counter

X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())

# x座標とy座標をそれぞれカウント
x_counter = Counter([X1, X2, X3])
y_counter = Counter([Y1, Y2, Y3])

# 各軸で1回しか出てこない（=残りの1点の座標）
for x in x_counter:
    if x_counter[x] == 1:
        X4 = x
        break

for y in y_counter:
    if y_counter[y] == 1:
        Y4 = y
        break

# 結果出力
print(X4, Y4)
