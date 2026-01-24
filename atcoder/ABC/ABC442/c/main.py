N, M = map(int, input().split())

if N <= 5:
    print(" ".join(["0"] * N))
    exit()

d = [set() for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    d[A].add(B)
    d[B].add(A)


def comb3(x):
    if x < 3:
        return 0
    return x * (x - 1) * (x - 2) // 6


ans = []

for i in range(N):
    non = N - 1 - len(d[i])
    ans.append(str(comb3(non)))

print(" ".join(ans))
