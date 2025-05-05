N, T = map(int, input().split())
scores = [0] * N  # 各選手の得点
score_counts = {0: N}  # 得点ごとの人数

for _ in range(T):
    A_i, B_i = map(int, input().split())
    A_i -= 1  # 0-indexedに変換

    # 変動前の得点のデクリメント
    old = scores[A_i]
    score_counts[old] -= 1

    # 変動前の得点を持つ選手が他にいない
    if score_counts[old] == 0:
        del score_counts[old]

    # 変動後の時点のインクリメント
    scores[A_i] += B_i
    new = scores[A_i]
    score_counts[new] = score_counts.get(new, 0) + 1

    print(len(score_counts))
