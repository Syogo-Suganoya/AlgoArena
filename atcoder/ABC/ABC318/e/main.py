N = int(input())
A = list(map(int, input().split()))

# 値ごとに累積の「添字の合計(sum)」と「出現回数(size)」を管理
sum_dict = {}
size_dict = {}

ans = 0

for k, x in enumerate(A, start=1):  # k は 1 から N
    s = size_dict.get(x, 0)
    sm = sum_dict.get(x, 0)

    ans += (k - 1) * s - sm - (s * (s - 1) // 2)

    size_dict[x] = s + 1
    sum_dict[x] = sm + k

print(ans)
