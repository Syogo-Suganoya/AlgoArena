from collections import defaultdict

# N: 数列の長さ, K: 求めたい部分和
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の出現回数を記録する辞書
count = defaultdict(int)
count[0] = 1  # 初期状態として、累積和0が1回出現していると考える

ans = 0  # 答え（部分和がKになる区間の個数）
cum_sum = 0  # 現在までの累積和

for a in A:
    cum_sum += a  # ここまでの累積和を更新

    # cum_sum - K が過去に何回出ていたかを数える
    # cum_sum - K = 過去の累積和のとき、現在の cum_sum との差が K になるから
    ans += count[cum_sum - K]

    # 現在の累積和の出現回数を増やす
    count[cum_sum] += 1

# 結果出力
print(ans)
