from heapq import heappop, heappush

# 入力: 駅数 n, 路線数 m
n, m = map(int, input().split())
ldkcab = [list(map(int, input().split())) for _ in range(m)]

# ans[i] = 駅 i に「到達できる最も遅い時刻」
# 初期は未到達を -inf としておく
ans = [float("-inf")] * n

# 逆向きグラフを構築
# 本来 A→B の路線を B→A として持つ
# （ゴールから遡るため）
g = [[] for _ in range(n)]
for l, d, k, c, a, b in ldkcab:
    g[b - 1].append((a - 1, l, d, k, c))

    # 終点 N から到達できる最大の時刻を初期化
    # 路線 (A→N) があるなら、出発側 A への最大到達時刻を求められる
    if b == n:
        # 最も遅い列車 = l + (k-1)*d
        # その駅を出発できるのは c 時間前に到着していないといけないので +c
        ans[-1] = max(ans[-1], l + (k - 1) * d + c)

# 優先度付きキュー (大きい時刻優先にしたいので -t で管理)
q = [(-ans[-1], n - 1)]

while q:
    t, u = heappop(q)  # t は負の値で入れてあるので注意
    t = -t

    # 駅 u から逆に伸ばす
    for v, l, d, k, c in g[u]:
        # ans[u] が小さすぎるとそもそも列車に乗れない
        # （最初の列車が l 発、乗車には c 以上の余裕が必要なので ans[u] >= c+l でないとダメ）
        if ans[u] < c + l:
            continue

        # ans[u] の範囲で乗れる「最も遅い列車」の発車時刻を計算
        # (ans[u]-c-l)//d = 乗れる本数 -1
        # k-1 と比較して小さい方を選び、その分だけ d を足す
        t = l + min((ans[u] - c - l) // d, k - 1) * d

        # 既にもっと遅い時刻で到達できていたら更新不要
        if ans[v] >= t:
            continue

        # 更新してキューに入れる
        ans[v] = t
        heappush(q, (-t, v))

# 出力: 1..N-1 の駅について最遅到達時刻を出す
# 到達不可なら "Unreachable"
for i in range(n - 1):
    if ans[i] == float("-inf"):
        print("Unreachable")
    else:
        print(ans[i])
