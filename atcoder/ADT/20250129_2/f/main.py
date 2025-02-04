N = int(input())
L = 12
r = [int("1" * (i + 1)) for i in range(L)]
s = set()
for i in range(L):
    for j in range(L):
        for k in range(L):
            s.add(r[i] + r[j] + r[k])
print(sorted(s)[N - 1])
