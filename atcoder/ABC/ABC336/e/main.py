N = int(input())
digits = list(map(int, str(N)))  # 入力 N を各桁の配列に変換
L = len(digits)  # 桁数


def count_good(s: int) -> int:
    """
    与えられた桁和 s に対して、
    - 桁和がちょうど s
    - かつその数が s で割り切れる
    という N 以下の整数の個数を数える関数
    """

    # dp[pos][sm][mod][tight]
    # pos   : 今見ている桁位置 (0〜L)
    # sm    : 現在までの桁和
    # mod   : 現在までに作った数の s での余り
    # tight : N の prefix と一致しているか (1=一致中, 0=自由)
    dp = [[[[0] * 2 for _ in range(s)] for __ in range(s + 1)] for ___ in range(L + 1)]

    dp[0][0][0][1] = 1  # まだ何も選んでいない状態

    # 桁 DP のループ
    for pos in range(L):  # 各桁を左から処理
        for sm in range(s + 1):  # 桁和
            for mod in range(s):  # 余り
                for tight in range(2):  # N 以下制約
                    now = dp[pos][sm][mod][tight]
                    if now == 0:
                        continue

                    # 次の桁の最大値 (tight の場合は N の桁に制限される)
                    limit = digits[pos] if tight else 9

                    for d in range(limit + 1):  # 次に選ぶ桁
                        if sm + d > s:  # 桁和がオーバーしたら無効
                            continue

                        # tight の更新:
                        #   これまで一致中 (tight=1) かつ d==limit なら次も一致
                        #   それ以外は N 未満確定 (tight=0)
                        ntight = tight and (d == limit)

                        # 遷移先を加算
                        dp[pos + 1][sm + d][(mod * 10 + d) % s][ntight] += now

    # 最後に「桁和が s」「mod==0 (割り切れる)」の数を数える
    return dp[L][s][0][0] + dp[L][s][0][1]


ans = 0
# 桁和 s の候補は最大でも 9 * L
for s in range(1, 9 * L + 1):
    ans += count_good(s)

print(ans)
