N, K = map(int, input().split())
A = list(input().split())

res = A[-K:] + A[: N - K]
print(" ".join(res))
