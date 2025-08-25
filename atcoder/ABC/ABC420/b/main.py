N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]

l = [0] * N

for i in range(M):
    ones = []
    zeros = []

    for j in range(N):
        if A[j][i] == 1:
            ones.append(j)
        else:
            zeros.append(j)

    if len(ones) == 0 or len(zeros) == 0:
        l = [x + 1 for x in l]
        continue

    if len(ones) <= len(zeros):
        for k in ones:
            l[k] += 1
    else:
        for k in zeros:
            l[k] += 1

max_val = max(l)
res = [i + 1 for i in range(N) if l[i] == max_val]
print(*res)
