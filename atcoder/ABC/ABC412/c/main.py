import bisect


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 1:
        print(1)
        return

    # 左端と右端を除いた中間ドミノをソート
    middle = sorted(A[1:-1])
    ans = 1  # 左端は必ず倒す
    current = A[0]

    while True:
        # 現在のドミノで右端を倒せるか
        if current * 2 >= A[-1]:
            ans += 1
            break

        # 倒せる範囲内で最大値を二分探索
        idx = bisect.bisect_right(middle, current * 2) - 1

        if idx < 0:
            # 倒せる中間ドミノが存在しない
            print(-1)
            return

        # 倒すドミノを更新
        current = middle.pop(idx)
        ans += 1

    print(ans)


T = int(input())
for _ in range(T):
    solve()
