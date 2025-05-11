S = input()
res = 0
for i, c in enumerate(S[::-1]):
    d = ord(c) - ord("A") + 1
    res += d * (26**i)
print(res)
