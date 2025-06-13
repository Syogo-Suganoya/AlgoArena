N = int(input())
A = list(map(int, input().split()))

k = 0
for i in range(N - 1):
    S, T = map(int, input().split())
    k = (A[i] + k) // S * T
print(A[-1] + k)
