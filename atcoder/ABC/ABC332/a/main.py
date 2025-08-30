N, S, K = map(int, input().split())

total = 0
for _ in range(N):
    A, B = map(int, input().split())
    total += A * B

if total < S:
    total += K

print(total)
