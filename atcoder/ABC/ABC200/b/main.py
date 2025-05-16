N, K = map(int, input().split())
n = N
for i in range(K):
    d, m = divmod(n, 200)
    if m == 0:
        n = d
        continue
    n = int(str(n) + "200")
print(n)
