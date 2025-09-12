import heapq
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
rates = [0] * N
belongs = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    rates[i] = a
    belongs[i] = b - 1  # 0-index に変換

# 各幼稚園ごとのヒープ（最大値を欲しいので -rate を使う）
kindergartens = [[] for _ in range(2 * 10**5)]
for i in range(N):
    heapq.heappush(kindergartens[belongs[i]], (-rates[i], i))

# 全幼稚園の最大値を管理するヒープ
max_rates = []
for k in range(len(kindergartens)):
    if kindergartens[k]:
        r, idx = kindergartens[k][0]
        heapq.heappush(max_rates, (-r, k))  # r は負なので反転して正に戻す


def clean(k):
    """幼稚園 k のヒープのトップを正しく保つ"""
    while kindergartens[k]:
        r, idx = kindergartens[k][0]
        if belongs[idx] != k:  # 既に別の幼稚園に移っていたら捨てる
            heapq.heappop(kindergartens[k])
        else:
            return (-r, k)
    return None


for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    old = belongs[c]
    new = d - 1

    # 新しい幼稚園に入れる
    belongs[c] = new
    heapq.heappush(kindergartens[new], (-rates[c], c))

    # 古い幼稚園の更新
    res_old = clean(old)
    if res_old:
        heapq.heappush(max_rates, res_old)

    # 新しい幼稚園の更新
    res_new = clean(new)
    if res_new:
        heapq.heappush(max_rates, res_new)

    # 全体の最小を出力
    while True:
        r, k = max_rates[0]
        # トップが最新のものか確認
        valid = clean(k)
        if valid and valid[0] == r:
            print(r)
            break
        else:
            heapq.heappop(max_rates)
