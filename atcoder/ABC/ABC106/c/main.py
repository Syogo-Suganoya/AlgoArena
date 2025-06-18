S = input()
K = int(input())

# 先頭の1の個数を数える
count_1 = 0
first_non1 = "1"  # 初期は1としておく（見つからなければ1出力）

for c in S:
    if c == "1":
        count_1 += 1
    else:
        first_non1 = c
        break  # 最初に出てきた1以外の文字で止める

# 判定
if count_1 >= K:
    print(1)
else:
    print(first_non1)
