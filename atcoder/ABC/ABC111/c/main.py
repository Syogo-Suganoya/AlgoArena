from collections import Counter

N = int(input())
V = list(map(int, input().split()))

# 偶数番目と奇数番目で分割
even_vals = [V[i] for i in range(0, N, 2)]
odd_vals = [V[i] for i in range(1, N, 2)]

ce = Counter(even_vals)
co = Counter(odd_vals)


# 出現回数の多い順に上位2つずつ取得
# 無い場合には (value, 0) の形にしておく
def top2(counter):
    items = counter.most_common(2)
    if len(items) == 1:
        items.append((None, 0))
    return items  # [(val1, cnt1), (val2, cnt2)]


(e1, ec1), (e2, ec2) = top2(ce)
(o1, oc1), (o2, oc2) = top2(co)

# 偶数の数・奇数の数
ne = len(even_vals)
no = len(odd_vals)

# ケース1：最頻値が異なるならそれでOK
if e1 != o1:
    ans = (ne - ec1) + (no - oc1)
    print(ans)
    exit()

# ケース2：最頻値が同じ → 2番目候補を使う
# パターンA：偶数側を2位に変更
a = (ne - ec2) + (no - oc1)
# パターンB：奇数側を2位に変更
b = (ne - ec1) + (no - oc2)

print(min(a, b))
