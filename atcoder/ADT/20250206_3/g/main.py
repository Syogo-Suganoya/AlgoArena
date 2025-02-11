from collections import defaultdict

# 入力の受け取り
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の初期化
current_sum = 0
count_map = defaultdict(int)
count_map[0] = 1  # S[0] = 0 は初期状態として1回現れると仮定
result = 0

# 累積和を計算し、条件を満たす区間の数をカウント
for num in A:
    current_sum += num
    result += count_map[current_sum - K]
    count_map[current_sum] += 1

# 結果の出力
print(result)
