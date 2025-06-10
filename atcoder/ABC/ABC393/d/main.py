N = int(input())
S = input().strip()


def main():
    # '1' の位置をすべて取得（0-indexed）
    pos = [i for i, c in enumerate(S) if c == "1"]

    # '1' がなければスワップ不要
    if not pos:
        print(0)
        return

    m = len(pos)  # '1' の個数
    mid = m // 2  # 中央のインデックス（0-index）

    # ターゲットとなる「1の塊」の開始位置は、
    # 中央に対応する pos[mid] を中心として配置する
    center = pos[mid]

    # そこへ寄せるために必要な swap 回数を合計する
    ans = 0
    for idx, p in enumerate(pos):
        # 目標位置は center - (mid - idx)
        target = center - (mid - idx)
        ans += abs(p - target)

    print(ans)


main()
