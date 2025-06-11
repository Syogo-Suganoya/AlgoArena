N, K = map(int, input().split())

A = list(map(int, input().split()))

empty_sheets = K  # はじめ、空席は K 個
start_count = 0  # スタートした回数は 0 回

for a in A:
    if empty_sheets < a:  # 空席が足りなければ
        start_count += 1  # スタートして
        empty_sheets = K  # 空席を K 個にする
    empty_sheets -= a  # a 人座る

start_count += 1  # 最後に 1 回スタートする

print(start_count)
