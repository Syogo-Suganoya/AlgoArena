a, b, k = list(map(int, input().split()))
i = 0
if a < b:
    while a < b:
        a *= k
        i += 1
    print(i)
else:
    print(0)
