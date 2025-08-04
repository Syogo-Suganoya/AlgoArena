mod = 10**9 + 7
N = int(input())

total = pow(10, N, mod)  # 全体: 10^N
no_zero = pow(9, N, mod)  # 0を含まない: 9^N
no_nine = pow(9, N, mod)  # 9を含まない: 9^N
no_zero_nine = pow(8, N, mod)  # 0も9も含まない: 8^N

ans = (total - 2 * no_zero + no_zero_nine) % mod
print(ans)
