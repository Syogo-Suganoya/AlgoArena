def cals(string, target):
    """
    文字列 string と target の前方一致する部分の長さを計算する。
    """
    for index in range(len(target)):
        if index >= len(string):
            return len(string)
        if string[index] != target[index]:
            return index
    return len(target)


# 入力
N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

# 各文字列について前方一致の長さを計算
prefix_lengths = [cals(S[i], T) for i in range(N)]

# target を反転して後方一致の長さを計算
T_reversed = T[::-1]
suffix_lengths = [cals(S[i][::-1], T_reversed) for i in range(N)]


def f(current_string, prefix_lengths, suffix_lengths):
    current_len = len(current_string)
    T_len = len(T)
    match_len = prefix_lengths + suffix_lengths

    # 完全一致する場合
    if prefix_lengths == current_len and current_len == T_len:
        return True

    # S が1文字多い
    if match_len >= current_len and current_len + 1 == T_len:
        return True

    # T が1文字多い
    if match_len >= T_len and T_len + 1 == current_len:
        return True

    # S と T の長さが同じで、1文字だけ置換すれば一致する場合
    if match_len == current_len - 1 and current_len == T_len:
        return True


# 条件を満たすインデックスを探す
valid_indices = []
for i in range(N):
    current_string = S[i]

    if f(S[i], prefix_lengths[i], suffix_lengths[i]):
        valid_indices.append(i + 1)

# 結果の出力
print(len(valid_indices))
print(" ".join(map(str, valid_indices)))
