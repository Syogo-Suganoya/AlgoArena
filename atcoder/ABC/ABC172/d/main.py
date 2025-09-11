N = int(input())
ans = 0
for i in range(1, N + 1):
    # i が N 以下の整数に何回現れるか（i の倍数の個数）
    k = N // i
    # i の貢献 = i * (1 + 2 + ... + k)
    ans += i * (k * (k + 1) // 2)
print(ans)
