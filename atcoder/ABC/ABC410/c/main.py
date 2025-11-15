N, Q = map(int, input().split())

# 初期配列
A = list(range(1, N + 1))

# 先頭のズレ（ローテート量）
offset = 0

for _ in range(Q):
    query = input().split()
    t = int(query[0])

    if t == 1:
        # タイプ1: A_p を x に更新
        p = int(query[1]) - 1  # 1-index → 0-index
        x = int(query[2])
        idx = (p + offset) % N  # 実際の位置に変換
        A[idx] = x

    elif t == 2:
        # タイプ2: A_p を出力
        p = int(query[1]) - 1
        idx = (p + offset) % N
        print(A[idx])

    else:
        # タイプ3: 配列を k 回ローテート
        k = int(query[1])
        offset = (offset + k) % N
