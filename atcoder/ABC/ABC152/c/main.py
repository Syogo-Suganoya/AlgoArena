N = int(input())
A = list(map(int, input().split()))

m = A[0]
res = 1

for i in range(1, N):
    if A[i] < m:
        res += 1
        m = A[i]

print(res)
