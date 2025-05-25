N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

# 累積和のための配列を用意（0番目は0としておく）
Bl = [0] * (N + 1)  # 黒玉の累積和
Wl = [0] * (M + 1)  # 白玉の累積和
maxW = [0] * (M + 1)  # ある範囲までの白玉の累積和の最大値を保持

# 黒玉の累積和を計算
for i in range(N):
    Bl[i + 1] = Bl[i] + B[i]

# 白玉の累積和を計算
# さらにmaxWでこれまでの最大累積和も管理
for i in range(M):
    Wl[i + 1] = Wl[i] + W[i]
    maxW[i + 1] = max(maxW[i], Wl[i + 1])

ans = 0
# 黒玉からi個選ぶときの価値の合計を試す
for i in range(N + 1):
    # 白玉は黒玉の個数以下まで選べるのでmin(i, M)
    # maxW[min(i, M)]で最大の価値の白玉を選ぶ組み合わせを加える
    ans = max(ans, Bl[i] + maxW[min(i, M)])

print(ans)
