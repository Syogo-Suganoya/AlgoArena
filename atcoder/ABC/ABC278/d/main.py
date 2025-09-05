from collections import defaultdict

# 入力
N = int(input())
A = list(map(int, input().split()))

# 状態管理
global_value = -1  # 全体代入の値（まだなら -1）
increment_map = defaultdict(int)  # indexごとの個別加算値

# クエリ処理
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 配列全体に代入
        global_value = query[1]
        increment_map.clear()  # 個別加算はリセット
    elif query[0] == 2:
        # 個別加算
        idx, value = query[1], query[2]
        increment_map[idx - 1] += value
    else:  # query[0] == 3
        # 現在の値を出力
        idx = query[1]  # 0-index
        base = A[idx - 1]
        if global_value != -1:
            base = global_value
        print(base + increment_map[idx - 1])
