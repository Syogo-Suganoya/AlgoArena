N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

res = N * M * B
res += sum(A) * M
res += sum(C) * N
print(res)
