N = int(input())
A = list(map(int, input().split()))

res = 0
for i, a in enumerate(A, 1):
    for j in range(1, a + 1):
        s = str(i) + str(j)
        c = set(s)
        if len(c) == 1:
            res += 1
print(res)
