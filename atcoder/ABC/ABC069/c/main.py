N = int(input())
A = list(map(int, input().split()))

# カウント用変数
cnt4 = 0  # 4の倍数
cnt2 = 0  # 2の倍数（ただし4の倍数を除く）
cnt1 = 0  # 奇数

# 数列を分類する
for a in A:
    if a % 4 == 0:
        cnt4 += 1
    elif a % 2 == 0:
        cnt2 += 1
    else:
        cnt1 += 1

# ポイント：
# ・4の倍数の数を cnt4
# ・奇数の数を cnt1 とすると、
#    「cnt1 <= cnt4 + 1」 なら「Yes」
#    それ以外は「No」
# cnt2は、まとめてしまう。

if cnt1 <= cnt4 + (1 if cnt2 == 0 else 0):
    print("Yes")
else:
    print("No")
