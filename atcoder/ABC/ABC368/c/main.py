def main():
    _ = int(input())
    H = list(map(int, input().split()))

    T = 0  # ターン数

    for h in H:
        # 5ダメージ(1+1+3)のセット攻撃
        # (1+3+1)(3+1+1)のようにTがなんであれ、3つセットは必ず5になる
        sets = h // 5
        T += sets * 3
        h %= 5

        # 残りの体力を削る
        while h > 0:
            T += 1
            h -= 3 if T % 3 == 0 else 1

    print(T)


main()


def incorrect():
    """
    愚直解
    TLE
    """
    _ = int(input())
    H = list(map(int, input().split()))

    T = 0  # ターン数

    while H:
        T += 1
        value = 3 if T % 3 == 0 else 1  # 3ターンに1回は value = 3

        # 最も小さい値に value を適用
        H[0] -= value

        # もし 0 以下になったら削除（ポップ）
        if H[0] <= 0:
            H.pop(0)

    print(T)
