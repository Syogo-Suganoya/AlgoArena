N, Q = map(int, input().split())
A = list(map(int, input().split()))

cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + A[i]

# 回転量を管理
shift = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 配列を右に query[1] だけ回転
        c = query[1]
        shift = (shift + c) % N
    else:
        l, r = query[1] - 1, query[2] - 1  # 0-indexに変換
        # shift を考慮した実際のインデックス
        l = (l - shift + N) % N
        r = (r - shift + N) % N

        if l <= r:
            ans = cum[r + 1] - cum[l]
        else:
            # 区間が配列の境界を跨ぐ場合
            ans = cum[N] + cum[r + 1] - cum[l]
        print(ans)
