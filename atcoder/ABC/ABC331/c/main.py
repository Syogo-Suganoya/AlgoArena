N = int(input())
A = list(map(int, input().split()))

sa = sorted(A, reverse=True)
# 内部用
in_a = sa[0]
# 更新に使う用
out_a = 0

d = {}
d[sa[0]] = 0

# ソートされたsaを使って、各値未満の合計を辞書に記録
for i in range(1, N):
    if sa[i - 1] != sa[i]:
        out_a = in_a
    d[sa[i]] = out_a
    in_a += sa[i]

# Aの各値に対して、dから合計値を取得して出力
for i in A:
    print(d[i], end=" ")
