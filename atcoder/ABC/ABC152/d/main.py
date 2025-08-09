N = int(input())
c = [[0] * 10 for _ in range(10)]

for x in range(1, N + 1):
    s = str(x)
    i = int(s[0])
    j = int(s[-1])
    c[i][j] += 1

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        res += c[i][j] * c[j][i]

print(res)
