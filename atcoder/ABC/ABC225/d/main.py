N, Q = map(int, input().split())

# 前後リンク（ない場合は -1）
prev = [-1] * (N + 1)
nxt = [-1] * (N + 1)

for _ in range(Q):
    t = list(map(int, input().split()))

    if t[0] == 1:
        # 1 x y : x の後ろに y を連結
        _, x, y = t
        nxt[x] = y
        prev[y] = x

    elif t[0] == 2:
        # 2 x y : x と y の連結を切る
        _, x, y = t
        nxt[x] = -1
        prev[y] = -1

    else:
        # 3 x : x を含む編成を出力
        _, x = t

        # --- 1) 先頭まで戻る ---
        head = x
        while prev[head] != -1:
            head = prev[head]

        # --- 2) 先頭から順に列挙 ---
        res = []
        cur = head
        while cur != -1:
            res.append(cur)
            cur = nxt[cur]

        print(len(res), *res)
