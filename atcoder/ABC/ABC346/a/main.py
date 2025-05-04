N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    print(A[i] * A[i - 1])
