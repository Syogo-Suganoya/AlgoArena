# 入力：N は比較する文字列の個数、T は正しいとされる文字列
N, T = input().split()
N = int(N)

ans = []

for i in range(1, N + 1):
    S = input()  # i 番目の文字列を読み込む

    # 先頭から一致している文字数をカウント（mae: 前）
    pre = 0
    while pre < min(len(S), len(T)) and S[pre] == T[pre]:
        pre += 1

    # 末尾から一致している文字数をカウント（ushiro: 後ろ）
    suf = 0
    while suf < min(len(S), len(T)) and S[-1 - suf] == T[-1 - suf]:
        suf += 1

    # --- 編集距離が1以下かどうかの判定 ---

    # 同じ長さで1文字だけ違う（例: abc vs acc）
    if len(S) == len(T) and pre + suf >= len(S) - 1:
        ans.append(i)

    # S が1文字短くて、1文字挿入すれば T になる（例: ac vs abc）
    elif len(S) == len(T) - 1 and pre + suf >= len(S):
        ans.append(i)

    # S が1文字長くて、1文字削除すれば T になる（例: abdc vs abc）
    elif len(S) == len(T) + 1 and pre + suf >= len(T):
        ans.append(i)

# 出力：条件を満たす文字列の個数と、そのインデックス
print(len(ans))
print(*ans)
