H, W, N = map(int, input().split())

h = [0] * N
w = [0] * N
for i in range(N):
    h[i], w[i] = map(int, input().split())

# ord_h, ord_w : ピース番号の並び替え
# h[ord_h[i]] >= h[ord_h[i+1]]
# w[ord_w[i]] >= w[ord_w[i+1]]
ord_h = sorted(range(N), key=lambda x: -h[x])
ord_w = sorted(range(N), key=lambda x: -w[x])

ans_x = [-1] * N
ans_y = [-1] * N
used = [False] * N

ith = 0
itw = 0

for _ in range(N):
    # すでに使用済みなら飛ばす
    while used[ord_h[ith]]:
        ith += 1
    while used[ord_w[itw]]:
        itw += 1

    # ピース i が縦 H ブロック or 横 W ブロック
    if h[ord_h[ith]] == H:
        i = ord_h[ith]
    else:
        i = ord_w[itw]

    # 右下に置く（1-indexed座標）
    ans_x[i] = H - h[i] + 1
    ans_y[i] = W - w[i] + 1
    used[i] = True

    # 残り領域を更新
    if h[i] == H:
        W -= w[i]
    else:
        H -= h[i]

for i in range(N):
    print(ans_x[i], ans_y[i])
