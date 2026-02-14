from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# 右側カウント（最初は全部入れておく）
count_r = Counter(A)

# 左側カウント（最初は空）
count_l = Counter()

ans = 0

for j in range(N):
    # 今見ている値を右側から取り除く
    count_r[A[j]] -= 1

    # Aj が 5 の倍数のときだけ考える
    if A[j] % 5 == 0:
        t = A[j] // 5
        x = 7 * t
        y = 3 * t

        # j が最大の場合（左側）
        ans += count_l[x] * count_l[y]

        # j が最小の場合（右側）
        ans += count_r[x] * count_r[y]

    # 今の値を左側に追加
    count_l[A[j]] += 1

print(ans)
