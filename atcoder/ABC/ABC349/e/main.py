from functools import lru_cache

# --- 入力 ---
A = [list(map(int, input().split())) for _ in range(3)]
total = sum(sum(row) for row in A)  # 盤面全体の得点は奇数


# --- 勝敗判定関数 ---
def check_winner(state):
    """
    state: 長さ9のタプル。0=未使用, 1=高橋, 2=青木
    """
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # 横
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # 縦
        (0, 4, 8),
        (2, 4, 6),  # 斜め
    ]
    for i, j, k in lines:
        if state[i] and state[i] == state[j] == state[k]:
            return state[i]  # 1なら高橋勝ち, 2なら青木勝ち
    return 0  # まだ決着してない


# --- 再帰探索 with メモ化 ---
@lru_cache(maxsize=None)
def dfs(state, turn, score_t, score_a):
    """
    state : 長さ9のタプル (0=空, 1=高橋, 2=青木)
    turn  : 1=高橋のターン, 2=青木のターン
    score_t, score_a : これまでの得点
    return : Trueなら「高橋勝ち確定」、Falseなら「青木勝ち確定」
    """
    winner = check_winner(state)
    if winner == 1:  # 高橋がそろえた
        return True
    elif winner == 2:  # 青木がそろえた
        return False

    # まだ置けるマスがあるか
    if all(x != 0 for x in state):
        # 点数勝負。合計は奇数なので引き分けはない
        return score_t > score_a

    # 空きマスに置いて試す
    n = 9
    if turn == 1:  # 高橋のターン
        for idx in range(n):
            if state[idx] == 0:
                i, j = divmod(idx, 3)
                new_state = list(state)
                new_state[idx] = 1
                if dfs(tuple(new_state), 2, score_t + A[i][j], score_a):
                    return True  # 勝てる手が一つでもあれば勝ち
        return False  # どの手も負けに繋がるなら負け
    else:  # 青木のターン
        for idx in range(n):
            if state[idx] == 0:
                i, j = divmod(idx, 3)
                new_state = list(state)
                new_state[idx] = 2
                if not dfs(tuple(new_state), 1, score_t, score_a + A[i][j]):
                    return False  # 青木が必勝できる手があるなら高橋は負け
        return True  # 青木のすべての手を耐えきれれば高橋勝ち


# --- 実行 ---
init_state = tuple([0] * 9)
if dfs(init_state, 1, 0, 0):
    print("Takahashi")
else:
    print("Aoki")
