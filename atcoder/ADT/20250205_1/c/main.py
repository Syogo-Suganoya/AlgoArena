import string

S = list(input())

res = 0
pre = "A"
for c in string.ascii_uppercase:
    if c == "A":
        continue
    res += abs(S.index(c) - S.index(pre))
    pre = c

print(res)
