import math

N = int(input())
A = list(map(int, input().split()))

# 左側と右側の累積GCDを計算するリスト
L = [0] * (N + 2)
R = [0] * (N + 2)

for i in range(1, N + 1):
    L[i] = math.gcd(L[i - 1], A[i - 1])
for i in range(N, 0, -1):
    R[i] = math.gcd(R[i + 1], A[i - 1])

# 書き換え対象を除いたGCDの最大値を探索
ans = 0
for i in range(1, N + 1):
    g = math.gcd(L[i - 1], R[i + 1])
    ans = max(ans, g)

print(ans)
