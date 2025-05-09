import bisect

N = int(input())
a = list(map(int, input().split()))

# 累積和リスト cum を作る。cum[i] = (時刻, 累積睡眠時間)
cum = [(0, 0)]  # 初期値（時刻0, 睡眠時間0）
for i in range(N // 2):
    sleep_start = a[2 * i + 1]  # 寝た時刻
    sleep_end = a[2 * i + 2]  # 起きた時刻
    total_sleep = cum[-1][1] + sleep_end - sleep_start
    cum.append((sleep_end, total_sleep))
    # 例: [(0,0), (起床1, 累積1), (起床2, 累積2), ...]

# クエリ数
Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())

    # L, R それぞれの位置（cumの添字）を探す
    # cum[i][0] > L となる最小の i → i-1 がLの属する区間
    l = bisect.bisect_left(cum, (L, 10**9)) - 1
    r = bisect.bisect_left(cum, (R, 0)) - 1

    # 累積睡眠時間の差をとる
    ans = cum[r][1] - cum[l][1]

    # Lが睡眠時間帯の途中なら、寝始めてない部分を引く
    ans -= max(0, L - a[2 * l + 1])

    # Rが睡眠時間帯の途中なら、寝てるはずの時間を足す（まだ起きてない分）
    ans += max(0, R - a[2 * r + 1])

    print(ans)
