N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

ans, m, s = 0, 0, 0
for a in A[::-1]:
    ans += a * m + s
    m += 10 ** len(str(a))
    s += a
print(ans % MOD)
