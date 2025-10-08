# 入力：N×N の関係行列
N = int(input())
C = [input() for _ in range(N)]

from collections import deque

# BFS用のキュー
q = deque()

# 距離マトリックスを初期化
# -1 は未計算、0 は同じ頂点、1 は直接の関係
A = [[-1] * N for _ in range(N)]

# 同じ頂点の距離は0
for i in range(N):
    q.append([0, i, i])  # [距離, i, i]
    A[i][i] = 0

# 直接の関係をキューに追加
for i in range(N):
    for j in range(N):
        if i == j or C[i][j] == "-":
            continue
        # C[i][j] が '-' でなければ、距離1の関係とする
        q.append([1, i, j])
        A[i][j] = 1

# BFSで距離を広げる
while q:
    n, i, j = q.popleft()  # 現在の距離 n と頂点ペア (i, j)

    # 頂点 i に接続する s を探す
    for s in range(N):
        cs = C[s][i]  # s → i の関係文字
        if cs == "-":
            continue

        # 頂点 j に接続する t を探す
        for t in range(N):
            ct = C[j][t]  # j → t の関係文字
            if ct == "-" or cs != ct or A[s][t] != -1:
                # 関係が存在しないか文字が違うか、既に距離が決まっている場合はスキップ
                continue

            # s → t の距離を更新
            A[s][t] = n + 2
            q.append([n + 2, s, t])  # 次の距離としてキューに追加

# 結果出力
for i in range(N):
    print(*A[i])
