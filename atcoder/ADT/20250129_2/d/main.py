N = int(input())
S = list(map(int, input().split()))

res = []
pre = 0
for i in S:
    res.append(i - pre)
    pre = i

print(*res)
