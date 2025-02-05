N = input()

res = N[:3]
if len(N) > 3:
    res += "0" * (len(N) - 3)
print(res)
