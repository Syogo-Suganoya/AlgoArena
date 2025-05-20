from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)  # 各数値の出現回数をカウント
res = 0  # 削除した数の合計

# 出現回数をリスト化して、出現回数が少ない順に並べる
freqs = sorted(c.values())

# 今ある種類数と、残すべき種類数との差だけ削除する
remove_kinds = max(0, len(freqs) - k)

# 出現回数の少ないものから順に削除していく
res = sum(freqs[:remove_kinds])

print(res)
