N = int(input())
res = 0
for i in range(1, N + 1):
    res += (-1) ** i * i**3
print(res)
