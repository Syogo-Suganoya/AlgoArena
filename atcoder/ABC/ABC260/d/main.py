from bisect import bisect_left

N, K = map(int, input().split())
P = list(map(int, input().split()))

# 各カードが何ターン目に食べられたかを記録
ans = [-1] * (N + 1)

# 場にある山のトップカードの値を管理（ソート済み）
tops = []

# 各山のカードを管理
piles = dict()

for turn, card in enumerate(P, 1):
    # 引いたカードを置くべき山を探す
    idx = bisect_left(tops, card)
    if idx == len(tops):
        # 新しい山を作る
        tops.append(card)
        piles[card] = [card]
    else:
        # 既存の山に置く
        top_card = tops[idx]
        piles[card] = piles.pop(top_card)
        piles[card].append(card)
        tops[idx] = card

    # 山のサイズがKになったら、カードを食べる
    if len(piles[card]) == K:
        for c in piles[card]:
            ans[c] = turn
        tops.pop(bisect_left(tops, card))
        del piles[card]

# 結果を出力
for i in range(1, N + 1):
    print(ans[i])
