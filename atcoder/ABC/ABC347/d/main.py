def popcount(x):
    return bin(x).count("1")


def solve():
    a, b, C = map(int, input().split())
    cntC = popcount(C)

    # 解なしになる条件をまずチェック
    # popcount(C) は X と Y の 1 の合計から引ける最大数
    # また、X に a 個、Y に b 個の 1 をどう割り振るかの整合性も必要
    if cntC > a + b:
        print(-1)
        return
    if (a + b - cntC) % 2 != 0:
        print(-1)
        return
    diff = (a + b - cntC) // 2
    # それぞれが使える 1 の数を調整
    a_rem = a - diff
    b_rem = b - diff
    if a_rem < 0 or b_rem < 0:
        print(-1)
        return

    X = 0
    Y = 0

    # C の 1 ビットに対して X または Y に 1 を割り振る
    for i in range(60):
        bit = 1 << i
        if C & bit:
            if a_rem > 0:
                X |= bit
                a_rem -= 1
            else:
                Y |= bit
                b_rem -= 1

    # 残った diff 個を、C の 0 ビットに X, Y 両方 1 を置く形で埋める
    for i in range(60):
        if diff == 0:
            break
        bit = 1 << i
        if not (C & bit):
            X |= bit
            Y |= bit
            diff -= 1

    # 最後に popcount の整合性を確認
    if popcount(X) != a or popcount(Y) != b or (X ^ Y) != C:
        print(-1)
    else:
        print(X, Y)


solve()
