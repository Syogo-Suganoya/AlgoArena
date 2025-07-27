N = int(input())
A = list(map(int, input().split()))

res = [0] * N

for i, c in enumerate(A, 1):
    res[c - 1] = i

print(*res)
