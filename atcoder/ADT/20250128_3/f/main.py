n, m = map(int, input().split())  # n, m 入力
a = list(map(int, input().split()))  # a 入力

# 初期状態を設定
current_sum = 0  # 現在の部分列のSの和
total_sum = 0  # 現在の部分列のTの和

# 最初の部分列 (0 から m-1 の要素) を計算
for i in range(m):
    current_sum += (i + 1) * a[i]  # i + 1 番目の位置の要素を乗じて加算
    total_sum += a[i]  # 部分列の和を計算

# 現在の最大値を保存
max_sum = current_sum

# スライディングウィンドウを使って残りの部分列を計算
for i in range(n - m):
    # 部分列の最初の要素を取り除き、新しい要素を加える
    current_sum = current_sum - total_sum + m * a[m + i]
    total_sum = total_sum - a[i] + a[i + m]

    # 最大値を更新
    max_sum = max(max_sum, current_sum)

# 結果を出力
print(max_sum)
