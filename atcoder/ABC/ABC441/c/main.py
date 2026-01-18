N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

# prefix_sum[i]: A[0] 〜 A[i-1] の合計
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

# ----------------------------
# まず「そもそも可能か？」の判定
# ----------------------------

# K個すべてが当たりだとしても、上位K個の合計がX未満なら不可能
if prefix_sum[K] < X:
    # 逆に「最悪ケース」＝下位K個を引いた場合でもX未満なら不可能
    if prefix_sum[N] - prefix_sum[N - K] < X:
        print("-1")
        exit()

non = N - K

# 二分探索の範囲
low = 1
high = N
ans = -1


# ----------------------------
# 判定関数
# mid個選んだとき、最悪でもX以上取れるか？
# ----------------------------
def f(mid):
    # mid個選んだとき、
    # そのうち確実に当たりになる個数
    L = mid - non

    # まだ全部ハズレの可能性がある
    if L <= 0:
        hit = 0
        return False
    else:
        # 「当たり確定分」は
        # A[non] 〜 A[mid-1] を取らされる（最悪ケース）
        hit = prefix_sum[mid] - prefix_sum[non]
        return hit >= X


# ----------------------------
# 二分探索
# ----------------------------
while low <= high:
    mid = (low + high) // 2

    if f(mid):
        # mid個で保証できる → もっと少なくできるか試す
        ans = mid
        high = mid - 1
    else:
        # まだ足りない → もっと選ぶ必要がある
        low = mid + 1

print(ans)
