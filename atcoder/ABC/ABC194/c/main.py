from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter()
sum_a = 0  # それまでに登場した数の合計
sum_a2 = 0  # それまでに登場した数の二乗の合計

ans = 0

for a in A:
    # 今まで出てきた要素すべてとの (a - x)^2 を計算
    # 和は: n * a^2 - 2a * Σx + Σx^2
    ans += cnt.total() * a * a - 2 * a * sum_a + sum_a2

    cnt[a] += 1
    sum_a += a
    sum_a2 += a * a

print(ans)
