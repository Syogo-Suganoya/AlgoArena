N = int(input())
p = list(map(int, input().split()))

res = 0
a = 0
for i, c in enumerate(p, 1):
    if i == c:
        a += 1
        if a % 2 == 1:
            res += 1
    else:
        a = 0
print(res)
