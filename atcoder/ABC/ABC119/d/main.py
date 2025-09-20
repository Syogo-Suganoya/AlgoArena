import bisect

# 入力
A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]  # 神社
T = [int(input()) for _ in range(B)]  # 寺
X = [int(input()) for _ in range(Q)]  # クエリ

S.sort()
T.sort()

INF = 10**18

for x in X:
    ans = INF

    # 神社の候補: x の左と右
    si = bisect.bisect_left(S, x)
    s_candidates = []
    if si > 0:
        s_candidates.append(S[si - 1])
    if si < A:
        s_candidates.append(S[si])

    # 寺の候補: x の左と右
    ti = bisect.bisect_left(T, x)
    t_candidates = []
    if ti > 0:
        t_candidates.append(T[ti - 1])
    if ti < B:
        t_candidates.append(T[ti])

    # 全組合せをチェック
    for s in s_candidates:
        for t in t_candidates:
            # 神社→寺
            d1 = abs(x - s) + abs(s - t)
            # 寺→神社
            d2 = abs(x - t) + abs(t - s)
            ans = min(ans, d1, d2)

    print(ans)
