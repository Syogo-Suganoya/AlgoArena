MOD = 10**9 + 7

W = int(input())

# 1列目の12通り × 2列目以降の7^(W-1)通り
ans = 12 * pow(7, W - 1, MOD) % MOD

print(ans)
