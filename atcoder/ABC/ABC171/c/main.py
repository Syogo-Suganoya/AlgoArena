N = int(input())
res = []
while N > 0:
    N -= 1
    res.append(chr(ord("a") + N % 26))
    N //= 26
print("".join(reversed(res)))
