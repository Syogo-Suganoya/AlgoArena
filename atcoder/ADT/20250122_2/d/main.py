N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

a = 1
for index in range(1, N + 1):
    j = index
    if j > a:
        a, j = j, a
    a = A[a - 1][j - 1]
print(a)
