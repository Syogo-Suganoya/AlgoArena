N = int(input())
A = list(map(int, input().split()))

UPPER = 2 * 10**5

# 数字 i がAの中に何回出てくるか
cnt = [0] * (UPPER + 1)
for i in range(N):
    cnt[A[i]] += 1

# i以下の数字の個数
for i in range(UPPER):
    cnt[i + 1] += cnt[i]

ans = 0

# Aの各要素 A[j] を「真ん中の数」として固定して考える
for j in range(N):
    # A[j] より小さい数がいくつあるか（左側）
    left = cnt[A[j] - 1]

    # A[j] より大きい数がいくつあるか（右側）
    right = N - cnt[A[j]]

    # A[i] < A[j] < A[k] となるような i, j, k の組の数を加算
    ans += left * right

print(ans)
