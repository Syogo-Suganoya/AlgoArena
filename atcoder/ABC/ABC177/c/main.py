MOD = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))

# 全要素の合計
total = sum(A) % MOD

ans = 0
for i in range(N):
    total = (total - A[i]) % MOD  # 自分の分を引く
    ans = (ans + A[i] * total) % MOD

print(ans)
