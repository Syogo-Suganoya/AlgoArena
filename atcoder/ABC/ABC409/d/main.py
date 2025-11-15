def solve():
    N = int(input())
    S = input()

    # 1. 最初に「降順になっている箇所」を探す
    l = -1
    for i in range(N - 1):
        if S[i] > S[i + 1]:
            l = i  # 移動する文字は S[l]
            break

    # 文字列がすでに辞書順通りならそのまま
    if l == -1:
        print(S)
        return

    # 2. S[l] を移動させる先の位置 r を探す
    r = N
    for j in range(l + 1, N):
        if S[l] < S[j]:
            r = j  # S[l] を r の直前に移動
            break

    # 3. 移動後の文字列を作る
    # S[:l] + S[l+1:r] + S[l] + S[r:]
    #   ↑元の S[l] を除いた範囲 + 移動した S[l] + 残り
    print(S[:l] + S[l + 1 : r] + S[l] + S[r:])


T = int(input())
for _ in range(T):
    solve()
