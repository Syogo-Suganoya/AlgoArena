N = int(input())
# 奇数の個数は (N + 1) // 2 で得られる
odd_count = (N + 1) // 2
# 確率は odd_count を N で割るのみ
print(odd_count / N)
