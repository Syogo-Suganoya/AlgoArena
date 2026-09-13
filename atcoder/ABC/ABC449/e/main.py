# 1. 入力部分 (ご指定の形式)
N, M = map(int, input().split())
A = list(map(int, input().split()))

# --- 事前準備 ---
# 各値 (1~M) の初期出現回数をカウント
counts = [0] * (M + 1)
for x in A:
    if 1 <= x <= M:
        counts[x] += 1

# 初期頻度ごとに値を分類
freq_buckets = [[] for _ in range(N + 1)]
for v in range(1, M + 1):
    if counts[v] <= N:
        freq_buckets[counts[v]].append(v)

# S[f]: 全てを頻度 f にするために必要な「追加回数」の合計
# S[f+1] = S[f] + (初期頻度が f 以下の要素数)
S = [0] * (N + 2)
num_elements_le = 0  # 初期頻度が f 以下の値の数
for f in range(N + 1):
    num_elements_le += len(freq_buckets[f])
    S[f + 1] = S[f] + num_elements_le

# --- クエリ処理 ---
Q = int(input())
queries = []
for i in range(Q):
    X = int(input())
    # X が N 以内なら初期配列 A から返すだけ
    if X <= N:
        queries.append((X, -1, i))  # (X, ターゲット頻度F, クエリID)
    else:
        K = X - N
        # 二分探索で「どの頻度レベルを埋めている最中か」を特定
        if K > S[N + 1]:
            # 全員が N+1 回以上になった後は、1~M の周期に入る
            rem = K - S[N + 1]
            ans_val = (rem - 1) % M + 1
            queries.append((ans_val, -2, i))
        else:
            # S[f] < K <= S[f+1] となる f を探す
            import bisect

            f = bisect.bisect_left(S, K) - 1
            rem = K - S[f]
            queries.append((rem, f, i))

# --- オフラインクエリ解決 (Fenwick Tree) ---
# 「初期頻度が f 以下の値の中で小さい方から m 番目」を高速に探す
ans = [0] * Q
bit = [0] * (M + 1)


def bit_add(idx, val):
    while idx <= M:
        bit[idx] += val
        idx += idx & (-idx)


def bit_kth(k):
    idx = 0
    for i in range(M.bit_length() - 1, -1, -1):
        nxt = idx + (1 << i)
        if nxt <= M and bit[nxt] < k:
            idx = nxt
            k -= bit[idx]
    return idx + 1


# ターゲット頻度 F が小さい順にクエリを処理 (Sweep-line)
queries.sort(key=lambda x: x[1])
curr_f = -1

for m_or_val, f, q_idx in queries:
    if f == -1:  # 初期配列
        ans[q_idx] = A[m_or_val - 1]
    elif f == -2:  # 周期モード
        ans[q_idx] = m_or_val
    else:
        # 必要な頻度 f まで BIT を更新
        while curr_f < f:
            curr_f += 1
            for v in freq_buckets[curr_f]:
                bit_add(v, 1)
        ans[q_idx] = bit_kth(m_or_val)

# 出力
print("\n".join(map(str, ans)))
