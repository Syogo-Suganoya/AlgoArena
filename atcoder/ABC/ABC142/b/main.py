# 入力の読み取り
N, K = map(int, input().split())
heights = list(map(int, input().split()))

# 条件を満たす人数を数える
count = 0
for h in heights:
    if h >= K:
        count += 1

# 結果を出力
print(count)
