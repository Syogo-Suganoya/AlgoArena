N, M = map(int, input().split())
S = list(map(int, input().split()))

c = N - M
print(c)

res = []
for i in range(1, N + 1):
    if i in S:
        continue
    res.append(str(i))

print(" ".join(res))
