N = int(input())
S = [int(input()) for _ in range(N)]

total = sum(S)  # すべての問題に正解した場合の合計得点

if total % 10 != 0:
    # 合計得点が10の倍数でなければ、そのまま表示される
    print(total)
else:
    # 合計得点が10の倍数の場合、10の倍数でない得点を持つ問題を探す
    S.sort()
    for s in S:
        if s % 10 != 0:
            # その問題を不正解とすることで、合計得点が10の倍数でなくなる
            print(total - s)
            break
    else:
        # すべての問題の得点が10の倍数である場合、表示される得点は0
        print(0)
