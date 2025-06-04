import bisect

V, A, B, C = map(int, input().split())

# A, B, C の1ターンあたりの消費合計
total = A + B + C

# Vを1ターン分の合計で割った余り（何ターンか回した後の残量）
V %= total

# 累積和を作成（A→B→Cの順で消費されるのでその順で累積）
cumsum = [A, A + B, A + B + C]

# bisect_rightで累積和のどこまで使われるかを探す
idx = bisect.bisect_right(cumsum, V)

# indexに応じて誰が使い切るかを判定
if idx == 0:
    print("F")
elif idx == 1:
    print("M")
else:
    print("T")
