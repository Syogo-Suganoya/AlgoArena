N = int(input())
A = list(map(int, input().split()))

INF = float("-inf")
dp_even = 0  # 偶数体倒したときの最大経験値
dp_odd = INF  # 奇数体倒したときの最大経験値

for a in A:
    new_dp_even = max(dp_even, dp_odd + 2 * a if dp_odd != INF else INF)
    new_dp_odd = max(dp_odd, dp_even + a)
    dp_even, dp_odd = new_dp_even, new_dp_odd

print(max(dp_even, dp_odd))
