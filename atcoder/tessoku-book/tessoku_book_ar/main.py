N, Q = map(int, input().split())
lst = [i for i in range(1, N + 1)]

rev = False  # 現在の向き（False＝正順、True＝反転）

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x, y = query[1:]
            x -= 1
            if rev:
                # 反転してるときは、後ろから数えるようにインデックス補正
                x = N - 1 - x
            lst[x] = y

        case 2:
            # 向きを反転（True ↔ False）
            rev = not rev

        case 3:
            x = query[1]
            x -= 1
            if rev:
                # 反転してるときは、出力も後ろから数える
                x = N - 1 - x
            print(lst[x])
