from collections import deque

# 右・下・左・上への移動ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 各マスの文字に対応する方向のビット XOR 用インデックス
# A -> 0, B -> 1, C -> 3
d = {"A": 0, "B": 1, "C": 3}


def solve():
    # グリッドの高さ h と幅 w を入力
    H, W = map(int, input().split())

    # グリッドの各行を入力
    S = [input() for i in range(H)]

    # dist[x][y][dir] : (x,y) に dir の向きで到達したときの最小コスト
    # 初期値は十分大きい値にしておく (ここでは 1<<30)
    dist = [[[1 << 30] * 4 for _ in range(W)] for _ in range(H)]

    dq = deque()
    # スタート位置 (0,0) はどの方向でもまだ未定なので -1
    # 初期コストは 1
    dq.append((0, 0, -1, 1))

    while dq:
        # 現在のコスト c, 位置 (pre_x, pre_y), 現在の方向 dir を取得
        c, pre_x, pre_y, dir = dq.popleft()

        # 現在の方向に従って次のマス (x, y) を計算
        x, y = pre_x + dx[dir], pre_y + dy[dir]

        # グリッド外ならスキップ
        if not (0 <= x < H and 0 <= y < W):
            continue

        # 次に進む方向を 4 方向で試す
        for ndir in range(4):
            # 180度ターンは無効（dir ^ ndir == 2 のとき）
            if dir ^ ndir == 2:
                continue

            # 現在のマスの文字に対応する方向と一致する場合、コスト 0
            if dir ^ ndir == d[S[x][y]]:
                if c < dist[x][y][ndir]:
                    dist[x][y][ndir] = c
                    # コスト 0 は deque の先頭に追加して優先度高め
                    dq.appendleft((c, x, y, ndir))
            else:
                # 一致しない場合はコスト +1
                if c + 1 < dist[x][y][ndir]:
                    dist[x][y][ndir] = c + 1
                    # コスト 1 は deque の末尾に追加
                    dq.append((c + 1, x, y, ndir))

    # 右方向でゴールに到達した最小コストを出力
    print(dist[H - 1][W - 1][1])


T = int(input())
for _ in range(T):
    solve()
