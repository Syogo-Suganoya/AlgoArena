from collections import deque

MOD = 998244353
Q = int(input())  # クエリの数

# deque（両端キュー）を使って数列を管理
dq = deque([1])  # 最初は「1」のみ
current_value = 1  # 数列を整数として見たときの現在の値

for _ in range(Q):
    query = input().split()

    if query[0] == "1":
        # クエリ「1 x」: 末尾に x を追加
        x = int(query[1])
        dq.append(x)
        # 新しい数字を末尾に追加すると、今までの数値は10倍される
        # 例: 123 → 1230 に x を加える: 1230 + x
        current_value = (current_value * 10 + x) % MOD

    elif query[0] == "2":
        # クエリ「2」: 先頭を削除
        removed_digit = dq.popleft()
        # 先頭の数字の重みを計算（10^(現在の長さ)）
        power = pow(10, len(dq), MOD)
        # 先頭の数字の寄与を引いて、新しい値にする
        current_value = (current_value - removed_digit * power) % MOD

    else:  # クエリ「3」
        # 現在の値を出力
        print(current_value)
