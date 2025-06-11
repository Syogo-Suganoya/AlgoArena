MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

# 累積和を準備
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = (S[i] + A[i]) % MOD

ans = 0
for j in range(N):
    d = len(str(A[j]))
    # 右辺の寄与
    ans = (ans + A[j] * j) % MOD
    # 左辺の寄与
    ans = (ans + S[j] * pow(10, d, MOD)) % MOD

print(ans)
