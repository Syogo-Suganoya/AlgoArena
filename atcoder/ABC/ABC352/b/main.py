S = input()
T = input()

l = 0
res = []
for c in S:
    l = T.find(c, l) + 1
    res.append(str(l))

print(*res)
