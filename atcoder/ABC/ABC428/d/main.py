import math

T = int(input())
for _ in range(T):
    c, d = map(int, input().split())
    ans = 0

    # xmin, xmax : D 側の数字範囲（1桁〜9桁までを10倍しながら広げていく）
    # cshift : C の右に付け足すための桁数を管理（10, 100, 1000...）
    xmin, xmax, cshift = 1, 9, 10

    # D の範囲 c+1 ～ c+d のうち、各桁ごとに処理
    while xmin <= c + d:
        # 今見ている桁範囲と c+1 ～ c+d の範囲の交差部分を求める
        l = max(xmin, c + 1)
        r = min(xmax, c + d)

        # l <= r のときにのみ有効範囲としてカウント
        if l <= r:
            # 実際に調べる数は「C を左側、l〜r を右側に連結した数」
            # つまり C*10^k + x 形式の整数
            vl = c * cshift + l
            vr = c * cshift + r

            # [vl, vr] の範囲内にある平方数の個数を求める
            # √vr - √(vl-1) がちょうど「その区間に含まれる平方数の個数」
            ans += int(math.isqrt(vr)) - int(math.isqrt(vl - 1))

        # 次の桁へ移動（例: 1〜9 → 10〜99 → 100〜999 ...）
        xmin *= 10
        xmax = (xmax + 1) * 10 - 1
        cshift *= 10

    print(ans)
