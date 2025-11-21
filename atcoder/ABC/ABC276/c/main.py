def previous_permutation(P):
    N = len(P)
    # 後ろから降下ポイントを探す
    i = N - 2
    while i >= 0 and P[i] <= P[i + 1]:
        i -= 1

    # 降下ポイントが見つからない場合は最小順列なのでそのまま
    if i < 0:
        return False

    # 右側で P[i] より小さい最大の値を探す
    j = N - 1
    while P[j] >= P[i]:
        j -= 1

    # 交換
    P[i], P[j] = P[j], P[i]

    # i+1 以降を逆順に
    P[i + 1 :] = reversed(P[i + 1 :])
    return True


N = int(input())
P = list(map(int, input().split()))

previous_permutation(P)

# 出力
print(*P)
