from collections import deque


def solve():
    n, m = map(int, input().split())
    nm = n * m

    # x, y：それぞれ「行に置きたい最大値」「列に置きたい最大値」
    # 1-index → 0-index に揃える
    x = [v - 1 for v in map(int, input().split())]
    y = [v - 1 for v in map(int, input().split())]

    # gx[v] = v を置くべき行番号
    # gy[v] = v を置くべき列番号
    # -1 なら「特に指定なし」
    gx = [-1] * nm
    gy = [-1] * nm

    # 行側の指定が重複していないか確認
    for i in range(n):
        if gx[x[i]] != -1:  # 同じ値が複数行から指定されたらアウト
            print("No")
            return
        gx[x[i]] = i

    # 列側の指定が重複していないか確認
    for j in range(m):
        if gy[y[j]] != -1:
            print("No")
            return
        gy[y[j]] = j

    # ok[v] = 「値 v を置くと queue に追加される空マス候補リスト」
    ok = [[] for _ in range(nm)]
    for i in range(n):
        for j in range(m):
            # min(x[i], y[j])：その行・列が要求する最大値より大きいものは置けない
            ok[min(x[i], y[j])].append((i, j))

    # 答えを入れる行列
    ans = [[-1] * m for _ in range(n)]

    # 条件を満たした後に埋めていくためのキュー
    q = deque()

    # v は置く値。大きい値から順に置いていく
    # 必ず高い値から配置しないと、制約に引っかかる
    for v in range(nm - 1, -1, -1):
        # 行指定も列指定もない値 v の場合
        if gx[v] == -1 and gy[v] == -1:
            # 置ける確定マスが無いのに要求されていればアウト
            if not q:
                print("No")
                return

            # queue に溜めていた候補マスに置く
            i, j = q.popleft()
            ans[i][j] = v + 1  # 出力は 1-index

            # この v より小さい値の候補を queue に積む
            for ii, jj in ok[v]:
                q.append((ii, jj))

            continue

        # 行か列どちらか一方にしか制約がないパターン
        if gx[v] == -1 or gy[v] == -1:
            # 配置可能マスがないならアウト
            if not ok[v]:
                print("No")
                return

            # ok[v] の中からひとつ取って配置する
            i, j = ok[v].pop()
            ans[i][j] = v + 1

            # 残りは queue に積む
            for ii, jj in ok[v]:
                q.append((ii, jj))

            continue

        # 行・列とも指定されている場合は一意に決まる
        i, j = gx[v], gy[v]
        ans[i][j] = v + 1

        # そのほかの候補は queue へ
        for ii, jj in ok[v]:
            if i != ii or j != jj:
                q.append((ii, jj))

    # 最後まで矛盾なし
    print("Yes")
    for r in ans:
        print(*r)


# 複数テストケース
for _ in range(int(input())):
    solve()
