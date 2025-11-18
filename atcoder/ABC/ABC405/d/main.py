from collections import deque

# 入力: 高さ H と幅 W
H, W = map(int, input().split())
# マップを2次元リストとして読み込む
S = [list(input()) for _ in range(H)]

# BFS用のキューを用意
Q = deque()
# マップ上の全ての 'E' の座標をキューに追加（スタート地点）
for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            Q.append((i, j))

# 移動方向の設定: 下, 右, 上, 左
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 移動方向に対応する文字
A = "^<v>"


# マップ内に収まるかをチェックする関数
def ok(i, j):
    return 0 <= i < H and 0 <= j < W


# BFS開始
while Q:
    i, j = Q.popleft()  # キューから1つ取り出す
    for k in range(4):  # 4方向をチェック
        ni, nj = i + dx[k], j + dy[k]  # 次の座標
        if not ok(ni, nj):
            continue  # マップ外ならスキップ
        if S[ni][nj] != ".":
            continue  # 壁や既に訪問済みならスキップ
        S[ni][nj] = A[k]  # 移動方向の矢印をセット
        Q.append((ni, nj))  # 次の探索対象に追加

# 結果の出力
for row in S:
    print("".join(row))
