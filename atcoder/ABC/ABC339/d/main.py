from collections import deque

# 上下左右の移動方向（右、左、下、上）
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

# --- 入力 ---
N = int(input())  # グリッドのサイズ
S = [input() for _ in range(N)]  # グリッド情報（'.' か '#' か 'P'）

# --- プレイヤーの初期位置を取得 ---
pi = pj = qi = qj = -1  # 初期化
for i in range(N):
    for j in range(N):
        if S[i][j] == "P":
            if (pi, pj) == (-1, -1):
                pi, pj = i, j  # 1人目の位置
            else:
                qi, qj = i, j  # 2人目の位置

# --- BFS用の距離配列 ---
# dist[y1][x1][y2][x2] : プレイヤー1が(y1,x1)、プレイヤー2が(y2,x2)にいるときの最短手数
# -1 : 未訪問
dist = [[[[-1] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
dist[pi][pj][qi][qj] = 0  # 初期状態は手数0

# --- BFSキュー ---
Q = deque([(pi, pj, qi, qj)])

while Q:
    y1, x1, y2, x2 = Q.popleft()

    # 2人が同じマスに到達したら最短手数を出力して終了
    if (y1, x1) == (y2, x2):
        exit(print(dist[y1][x1][y2][x2]))

    # 4方向の移動を試す
    for dy, dx in directions:
        # プレイヤー1の移動
        ny, nx = y1 + dy, x1 + dx
        if not (0 <= ny < N and 0 <= nx < N) or S[ny][nx] == "#":
            ny, nx = y1, x1  # 壁または範囲外なら動かず

        # プレイヤー2の移動
        ny2, nx2 = y2 + dy, x2 + dx
        if not (0 <= ny2 < N and 0 <= nx2 < N) or S[ny2][nx2] == "#":
            ny2, nx2 = y2, x2  # 壁または範囲外なら動かず

        # 未訪問の状態ならキューに追加して手数を更新
        if dist[ny][nx][ny2][nx2] == -1:
            dist[ny][nx][ny2][nx2] = dist[y1][x1][y2][x2] + 1
            Q.append((ny, nx, ny2, nx2))

# BFS終了後も同じマスに到達できなければ -1
print(-1)
