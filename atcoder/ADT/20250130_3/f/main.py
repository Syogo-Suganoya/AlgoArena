N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
avg = sum_A // N
b = [avg for _ in range(0, N)]

for i in range(0, sum_A % N):
    b[(i + 1) * -1] += 1

A.sort()

ans = 0
for i in range(0, N):
    ans += abs(A[i] - b[i])

print(ans // 2)
