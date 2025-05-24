n, k = map(int, input().split())
s = k
a = [1 for i in range(n + 1)]
for i in range(k, n + 1):
    a[i] = s
    s -= a[i - k]
    s += a[i]
    s %= 1000000000
print(a[n])
