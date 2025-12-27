N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

PA = [0] * (N + 1)
PB = [0] * (N + 1)
PC = [0] * (N + 1)

for i in range(N):
    PA[i + 1] = PA[i] + A[i]
    PB[i + 1] = PB[i] + B[i]
    PC[i + 1] = PC[i] + C[i]

bestAB = [-(10**18)] * (N + 1)
for i in range(1, N):
    if i == 1:
        bestAB[i] = PA[i] - PB[i]
    else:
        bestAB[i] = max(bestAB[i - 1], PA[i] - PB[i])

ans = -(10**18)
for l2 in range(2, N):
    ans = max(ans, bestAB[l2 - 1] + PB[l2] - PC[l2])

ans += PC[N]
print(ans)
