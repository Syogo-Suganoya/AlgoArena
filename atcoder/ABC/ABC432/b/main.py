N = input().strip()

digits = list(map(int, N))
nonzero = [d for d in digits if d != 0]
first = min(nonzero)
digits.remove(first)
digits.sort()
res = str(first) + "".join(map(str, digits))

print(res)
