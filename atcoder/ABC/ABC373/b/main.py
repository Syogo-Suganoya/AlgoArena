S = input()

now = "A"
res = 0
for target in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    res += abs(S.index(now) - S.index(target))
    now = target
print(res)
