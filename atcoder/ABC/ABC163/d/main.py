MOD = 10**9 + 7

N, K = map(int, input().split())

ans = 0
low = 0  # 小さい方から選んだときの “追加部分” の累積最小値
high = 0  # 大きい方から選んだときの “追加部分” の累積最大値

for a in range(1, N + 2):  # a = 1 から N+1 個選ぶ場合
    # low に (a-1) を足す → これが a 個のときの最小の「i の和」
    low += a - 1
    # high に (N - (a-1)) を足す → i の最大側からの和
    high += N - (a - 1)

    if a >= K:
        # a 個選ぶとき、和の個数
        cnt = high - low + 1
        ans = (ans + cnt) % MOD

print(ans)
