N = int(input())
cards = [tuple(map(int, input().split())) for _ in range(N)]

# dp[状態] = 勝者（True: 先手の勝ち, False: 後手の勝ち）
# 状態は「どのカードが残っているか」をビットで表現する
# 例: N=4 の場合, state = 0b1101 → 0,2,3番のカードが残っている
dp = [-1] * (1 << N)
dp[0] = False  # すべてのカードが取り除かれた状態は「動けない」ので後手の勝ち


def can_remove(i, j):
    """
    2枚のカード i, j を同時に取り除けるかどうか判定する関数。
    ルール: a_i == a_j または b_i == b_j のときだけ取り除ける。
    """
    return cards[i][0] == cards[j][0] or cards[i][1] == cards[j][1]


def rec(state):
    """
    メモ化再帰で「state の状態で手番のプレイヤーが勝てるか」を判定する関数。
    True → 勝ち状態
    False → 負け状態
    """
    # すでに計算済みならその値を返す
    if dp[state] != -1:
        return dp[state]

    # 残っているカードから2枚選んで取り除けるか試す
    for i in range(N):
        if (state >> i) & 1:  # i番のカードが残っているか
            for j in range(i + 1, N):
                if (state >> j) & 1 and can_remove(i, j):
                    # i, j のカードを取り除いた次の状態を作る
                    next_state = state & ~(1 << i) & ~(1 << j)

                    # もし次の状態が「相手の負け状態」なら
                    # 自分はこの一手で勝ちが確定する
                    if not rec(next_state):
                        dp[state] = True
                        return True

    # どんな2枚を選んでも勝てなかった場合は負け状態
    dp[state] = False
    return False


# 初期状態（全カード残っている状態）から勝敗を判定
if rec((1 << N) - 1):
    print("Takahashi")  # 先手（高橋くん）の勝ち
else:
    print("Aoki")  # 後手（青木くん）の勝ち
