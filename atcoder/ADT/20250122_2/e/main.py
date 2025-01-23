n, a, b = map(int, input().split())
d = list(map(int, input().split()))

e = sorted([di % (a + b) for di in d])
e.append(e[0] + a + b)

for i in range(n):
    if e[i + 1] - e[i] > b:
        print("Yes")
        exit()

print("No")
