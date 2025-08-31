from collections import defaultdict
from fractions import Fraction as F
from functools import cache
from itertools import product

# サイコロの目（5個）を入力
A = list(map(int, input().split()))

# 出目の多重集合を確率付きで整理（今回は状態DPで直接使うわけではない）
deme = [defaultdict(lambda: F(0, 1)) for _ in range(6)]
for n in range(1, 6):
    deno = 6**n
    for idxs in product(range(6), repeat=n):
        deme[n][tuple(sorted(idxs))] += F(1, deno)


@cache
def f(rest_turn, keep_idxs):
    """
    残りターン rest_turn、キープ済みのサイコロインデックス keep_idxs
    の状態での最大期待値を返す
    """
    # すでに5個キープ済みならスコア計算
    if len(keep_idxs) == 5:
        count = defaultdict(int)
        for idx in keep_idxs:
            count[A[idx]] += 1
        # 得点は「同じ目の数 × 目の値」の最大
        return max(k * v for k, v in count.items())

    # まだ振っていないサイコロの数
    rest_dice = 5 - len(keep_idxs)
    ans = 0

    # 残りサイコロを振る場合の全パターン
    for deme_idxs in product(range(6), repeat=rest_dice):
        prob = F(1, 6**rest_dice)  # 出る確率
        M = 0
        # どのダイスをキープするか全探索
        # 最後のターンは全部キープする
        for keep in range(1 << rest_dice) if rest_turn != 1 else [(1 << rest_dice) - 1]:
            new_keep_idxs = tuple(
                sorted(
                    keep_idxs
                    + tuple(idx for i, idx in enumerate(deme_idxs) if (keep >> i) & 1)
                )
            )
            # 再帰で次状態の最大期待値を計算
            M = max(M, f(rest_turn - 1, new_keep_idxs))
        ans += M * prob  # 確率で重み付け

    return ans


# 初期状態：残り3ターン、キープなし
print(f"{float(f(3, tuple())):.10f}")
