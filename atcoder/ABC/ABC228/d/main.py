from sortedcontainers import SortedSet

# クエリ数の入力
Q = int(input())
query = []
for _ in range(Q):
    t, x = map(int, input().split())
    query.append((t, x))

N = 1 << 20  # 配列のサイズは 2^20 = 1048576
A = [-1 for _ in range(N)]  # 初期化された配列、すべて -1（未使用）

# 未使用のインデックスを管理するための SortedSet
# 最初は 0 〜 N-1 の全てが未使用
cand = SortedSet(range(N))

for t, x in query:
    if t == 2:
        # クエリタイプ2: x % N の位置の値を出力
        print(A[x % N])
        continue

    val = x
    x %= N  # ハッシュ関数: x mod N
    idx = cand.bisect_left(x)  # x 以上の最小の未使用インデックスを探す

    if idx < len(cand):
        pos = cand[idx]  # 使用する位置
    else:
        # x 以上の未使用インデックスが見つからなければ、配列の先頭に戻る
        pos = cand[0]

    A[pos] = val  # 値を格納
    cand.discard(pos)  # 使用済みのインデックスを削除
