N, K = map(int, input().split())

all = []
for _ in range(N):
    A, B = map(int, input().split())
    all.append(B)
    all.append(A - B)

all.sort()

print(sum(all[-K:]))
